import type { ImageMetadata } from 'astro';
import { getImage } from 'astro:assets';

/** Largeur maximale de la version HD affichée dans la lightbox. */
export const LARGEUR_HD = 2560;

export interface VersionHD {
  src: string;
  width: number;
  height: number;
}

/** Version HD (WebP, 2560 px de large au plus, jamais agrandie) pour la lightbox. */
export async function versionHD(image: ImageMetadata): Promise<VersionHD> {
  const width = Math.min(LARGEUR_HD, image.width);
  const hd = await getImage({ src: image, width, format: 'webp', quality: 'high' });
  return { src: hd.src, width, height: Math.round((image.height * width) / image.width) };
}
