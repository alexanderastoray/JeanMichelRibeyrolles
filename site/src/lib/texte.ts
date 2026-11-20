/** Découpe un texte de collection en strophes, puis en vers (lignes conservées telles quelles). */
export function strophes(texte: string): string[][] {
  return texte
    .trim()
    .split(/\n\s*\n/)
    .map((s) => s.split('\n').map((l) => l.trimEnd()));
}
