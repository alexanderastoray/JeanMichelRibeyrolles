import { defineCollection, reference } from 'astro:content';
import { glob, type Loader } from 'astro/loaders';
import { z } from 'astro/zod';

/* --------------------------------------------------------------------------
   Collections (les 4 séries d'œuvres)
   Identifiant = nom du fichier YAML = slug d'URL.
   -------------------------------------------------------------------------- */
const series = defineCollection({
  loader: glob({ pattern: '*.yaml', base: './src/content/collections' }),
  schema: ({ image }) =>
    z.object({
      titre: z.string().min(1),
      ordre: z.int().positive(),
      description: z.string().min(1).max(160),
      bandeau: image(),
      /** Point de cadrage du bandeau (object-position), valable en desktop et en mobile. */
      bandeauCadrage: z.string().regex(/^\d{1,3}% \d{1,3}%$/).default('50% 50%'),
      /** `vers` : un vers par ligne, strophes séparées par une ligne vide. `prose` : paragraphe. */
      typeTexte: z.enum(['vers', 'prose']),
      texte: z.string().min(1),
      /** Extrait affiché sur /collections/ (mêmes règles que `texte`). */
      extrait: z.string().min(1),
      /** Œuvres affichées sur /collections/, dans l'ordre ; elles peuvent appartenir à une autre collection. */
      apercu: z.array(reference('oeuvres')).min(1).max(4),
    }),
});

/* --------------------------------------------------------------------------
   Œuvres
   Identifiant = référence en minuscules (segment d'URL de la fiche).
   -------------------------------------------------------------------------- */
const cm = z.number().positive();

const dimensions = z
  .object({
    hauteur: cm.optional(),
    largeur: cm.optional(),
    profondeur: cm.optional(),
    diametre: cm.optional(),
    epaisseur: cm.optional(),
  })
  .strict()
  .superRefine((d, ctx) => {
    const issue = (message: string): void => {
      ctx.addIssue({ code: 'custom', message });
    };
    if (d.diametre !== undefined) {
      // Forme ronde : Ø × épaisseur
      if (d.epaisseur === undefined) issue('Forme ronde : « epaisseur » est obligatoire avec « diametre ».');
      if (d.hauteur !== undefined || d.largeur !== undefined || d.profondeur !== undefined) {
        issue('Forme ronde : « hauteur », « largeur » et « profondeur » sont interdites avec « diametre ».');
      }
    } else {
      // Forme rectangulaire : hauteur × largeur [× profondeur | × épaisseur]
      if (d.hauteur === undefined || d.largeur === undefined) {
        issue('Forme rectangulaire : « hauteur » et « largeur » sont obligatoires (ou « diametre » + « epaisseur »).');
      }
      if (d.profondeur !== undefined && d.epaisseur !== undefined) {
        issue('Forme rectangulaire : « profondeur » et « epaisseur » ne peuvent pas être renseignées ensemble.');
      }
    }
  });

/** Loader glob + vérification de l'unicité de `ordre` au sein de chaque collection. */
function oeuvresLoader(): Loader {
  const base = glob({
    pattern: '*.yaml',
    base: './src/content/oeuvres',
    generateId: ({ data, entry }) => {
      if (typeof data.ref !== 'string') throw new Error(`${entry} : champ « ref » manquant.`);
      return data.ref.toLowerCase();
    },
  });
  return {
    name: 'oeuvres-loader',
    load: async (context) => {
      await base.load(context);
      const vus = new Map<string, string>();
      const doublons: string[] = [];
      for (const { id, data } of context.store.values()) {
        const { collection, ordre } = data as { collection: { id: string }; ordre: number };
        const cle = `${collection.id}#${ordre}`;
        const autre = vus.get(cle);
        if (autre) doublons.push(`« ordre: ${ordre} » en double dans ${collection.id} (${autre}, ${id})`);
        else vus.set(cle, id);
      }
      if (doublons.length) throw new Error(`Œuvres : ${doublons.join(' ; ')}.`);
    },
  };
}

const oeuvres = defineCollection({
  loader: oeuvresLoader(),
  schema: ({ image }) =>
    z.object({
      ref: z.string().regex(/^[A-Z0-9]+$/, 'Référence en majuscules et chiffres, sans espace.'),
      collection: reference('collections'),
      /** Position dans la collection ; unique au sein d'une collection (vérifié au chargement). */
      ordre: z.int().positive(),
      format: z.enum(['murale', 'socle']),
      quatreMains: z.boolean().default(false),
      dimensions,
      materiaux: z.array(z.string().min(1)).min(1),
      annee: z.int().min(1990).max(2100).optional(),
      vues: z
        .array(z.object({ image: image(), type: z.enum(['ensemble', 'detail', 'autre']) }))
        .min(1)
        .max(6)
        .refine((v) => v[0]?.type === 'ensemble', 'La première vue doit être de type « ensemble ».'),
    }),
});

export const collections = { collections: series, oeuvres };
