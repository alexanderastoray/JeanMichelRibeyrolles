/** Matériaux affichés dans le cartel : « Frêne, inox ». */
export function materiauxCartel(materiaux: readonly string[]): string {
  const [premier = '', ...autres] = materiaux;
  return [premier, ...autres.map((m) => m.toLocaleLowerCase('fr-FR'))].join(', ');
}
