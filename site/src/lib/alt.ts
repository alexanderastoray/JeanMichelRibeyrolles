import { formaterDimensions, type Dimensions } from './dimensions';

/** « frêne et inox », « chêne, pin douglas et acier ». */
export function listerMateriaux(materiaux: readonly string[]): string {
  const m = materiaux.map((x) => x.toLocaleLowerCase('fr-FR'));
  return m.length <= 1 ? (m[0] ?? '') : `${m.slice(0, -1).join(', ')} et ${m.at(-1)}`;
}

interface AltOptions {
  collectionTitre: string;
  materiaux: readonly string[];
  dimensions: Dimensions;
  type: 'ensemble' | 'detail' | 'autre';
}

/**
 * Texte alternatif généré : collection + matériaux + dimensions.
 * « Les Miroirs d’Énigme : sculpture en frêne et inox, Ø 65 × 5 cm, détail »
 */
export function texteAlternatif({ collectionTitre, materiaux, dimensions, type }: AltOptions): string {
  const base = `${collectionTitre} : sculpture en ${listerMateriaux(materiaux)}, ${formaterDimensions(dimensions)}`;
  return type === 'detail' ? `${base}, détail` : type === 'autre' ? `${base}, autre vue` : base;
}
