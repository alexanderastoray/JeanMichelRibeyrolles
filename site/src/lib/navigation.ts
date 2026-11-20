export interface LienNav {
  href: string;
  label: string;
}

export const navigation: readonly LienNav[] = [
  { href: '/collections/', label: 'Collections' },
  { href: '/artelier/', label: "ART'elier" },
  { href: '/portrait/', label: 'Portrait' },
  { href: '/contact/', label: 'Contact' },
];

/** Vrai si `pathname` est la page `href` ou l'une de ses sous-pages. */
export function estActif(pathname: string, href: string): boolean {
  return pathname === href || pathname.startsWith(href);
}
