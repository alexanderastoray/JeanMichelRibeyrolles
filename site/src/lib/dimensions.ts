/** Dimensions en cm, telles que stockées dans les fichiers d'œuvre. */
export interface Dimensions {
  hauteur?: number | undefined;
  largeur?: number | undefined;
  profondeur?: number | undefined;
  diametre?: number | undefined;
  epaisseur?: number | undefined;
}

const nombre = new Intl.NumberFormat('fr-FR', { maximumFractionDigits: 2 });
const NBSP = ' ';

type Cote = { valeur: number; libelle: string };

/** Cotes dans l'ordre d'affichage : Ø × épaisseur, ou hauteur × largeur × (profondeur | épaisseur). */
function cotes(d: Dimensions): Cote[] {
  const liste: [number | undefined, string][] =
    d.diametre !== undefined
      ? [
          [d.diametre, 'diamètre'],
          [d.epaisseur, 'épaisseur'],
        ]
      : [
          [d.hauteur, 'hauteur'],
          [d.largeur, 'largeur'],
          [d.profondeur, 'profondeur'],
          [d.epaisseur, 'épaisseur'],
        ];
  return liste.filter((c): c is [number, string] => c[0] !== undefined).map(([valeur, libelle]) => ({ valeur, libelle }));
}

/** « Ø 65 × 5 cm », « 41 × 34 × 4,5 cm » (virgule décimale, espaces insécables). */
export function formaterDimensions(d: Dimensions): string {
  const texte = cotes(d)
    .map((c) => nombre.format(c.valeur))
    .join(`${NBSP}× `);
  return `${d.diametre !== undefined ? `Ø${NBSP}` : ''}${texte}${NBSP}cm`;
}

/** « diamètre × épaisseur », « hauteur × largeur × épaisseur »… */
export function libelleDimensions(d: Dimensions): string {
  return cotes(d)
    .map((c) => c.libelle)
    .join(' × ');
}
