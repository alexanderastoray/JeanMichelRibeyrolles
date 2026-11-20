import { getCollection, getEntry, type CollectionEntry } from 'astro:content';
import { texteAlternatif } from './alt';
import { formaterDimensions, libelleDimensions } from './dimensions';
import { materiauxCartel } from './cartel';

export type Oeuvre = CollectionEntry<'oeuvres'>;
export type Collection = CollectionEntry<'collections'>;
export type Vue = Oeuvre['data']['vues'][number];

/** Collections triées par `ordre`. */
export async function getCollections(): Promise<Collection[]> {
  return (await getCollection('collections')).sort((a, b) => a.data.ordre - b.data.ordre);
}

/** Œuvres d'une collection, triées par `ordre`. */
export async function getOeuvresDe(collectionId: string): Promise<Oeuvre[]> {
  return (await getCollection('oeuvres', (o) => o.data.collection.id === collectionId)).sort(
    (a, b) => a.data.ordre - b.data.ordre,
  );
}

export async function getCollectionDe(oeuvre: Oeuvre): Promise<Collection> {
  const c = await getEntry(oeuvre.data.collection);
  if (!c) throw new Error(`${oeuvre.data.ref} : collection « ${oeuvre.data.collection.id} » introuvable.`);
  return c;
}

/** Œuvres d'aperçu d'une collection, dans l'ordre déclaré. */
export async function getApercu(collection: Collection): Promise<Oeuvre[]> {
  return Promise.all(
    collection.data.apercu.map(async (r) => {
      const o = await getEntry(r);
      if (!o) throw new Error(`${collection.id} : œuvre d'aperçu « ${r.id} » introuvable.`);
      return o;
    }),
  );
}

export function urlCollection(collectionId: string): string {
  return `/collections/${collectionId}/`;
}

export function urlOeuvre(oeuvre: Oeuvre): string {
  return `/collections/${oeuvre.data.collection.id}/${oeuvre.id}/`;
}

/** Œuvres précédente et suivante dans la collection (circulaire). `null` si l'œuvre est seule. */
export function voisines(oeuvre: Oeuvre, liste: readonly Oeuvre[]): { precedente: Oeuvre; suivante: Oeuvre } | null {
  const i = liste.findIndex((o) => o.id === oeuvre.id);
  if (i < 0 || liste.length < 2) return null;
  const n = liste.length;
  return { precedente: liste[(i - 1 + n) % n]!, suivante: liste[(i + 1) % n]! };
}

/** « Dans la même collection » : jusqu'à `max` œuvres après l'œuvre courante (en boucle), sans elle. */
export function memeCollection(oeuvre: Oeuvre, liste: readonly Oeuvre[], max = 6): Oeuvre[] {
  const i = liste.findIndex((o) => o.id === oeuvre.id);
  const autres = [...liste.slice(i + 1), ...liste.slice(0, Math.max(i, 0))];
  return autres.slice(0, max);
}

/** Valeurs dérivées d'une œuvre, jamais stockées. */
export function derive(oeuvre: Oeuvre, collection: Collection) {
  const { dimensions, materiaux, vues } = oeuvre.data;
  const alt = (v: Vue): string =>
    texteAlternatif({ collectionTitre: collection.data.titre, materiaux, dimensions, type: v.type });
  return {
    url: urlOeuvre(oeuvre),
    dimensionsTexte: formaterDimensions(dimensions),
    dimensionsLibelle: libelleDimensions(dimensions),
    materiauxTexte: materiauxCartel(materiaux),
    vuePrincipale: vues[0]!,
    vueDetail: vues.find((v) => v.type === 'detail'),
    alt,
  };
}
