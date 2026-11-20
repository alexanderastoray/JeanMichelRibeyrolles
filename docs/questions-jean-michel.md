# Questions à valider avec Jean-Michel

Points ouverts sur les maquettes `maquettes/artelier.html` et `maquettes/contact.html` (19/11/2026).

## ART'elier

1. **Livre d'or : témoignages choisis.** La page en affiche 4, cités en entier, sans date :
   - Marine : « Un voyage à travers les matières, accompagné par une douce musique… »
   - Valère : « Un lieu unique. Un plaisir de regarder des pièces de plus en plus vivantes… »
   - Audrey : « Un régal pour les yeux, une vraie nourriture de l'âme… »
   - Chantal et Michel : « Jolie exposition. Très beau travail… »

   Ces 4 choix vous conviennent-ils ?

   Le témoignage de Patrick et Jacquie (« À Samonteil, derrière le rideau Home, nous sommes délicatement invités… ») pourrait remplacer l'un des quatre. Il serait alors cité en entier, avec la correction « invité » → « invités ».

   Tous les témoignages datent d'août et septembre 2020. Faut-il en ajouter de plus récents ?
2. **Photo des instruments de musique.** Un emplacement « Photo à venir » est prévu dans la partie « La musique ». Quelle photo fournir : les instruments seuls, ou Jean-Michel en train de jouer à l'ART'elier ?
3. **Exposition « Mémoire de Traces Oubliées – Espace Orlando ».** Elle n'apparaît plus comme rubrique : ses photos sont dans la galerie « L'univers en exposition », sans date. Faut-il la garder comme rubrique, avec sa date et le lieu complet (ville) ? Ou la déplacer vers une page d'expositions ?
4. **Origine des photos `20250826_*`.** Ont-elles été prises à l'Espace Orlando ou à l'ART'elier ? La galerie les présente sans lieu.
5. **Textes réécrits ou corrigés** (à relire) :
   - « Venez vous évader au milieu de ses œuvres, réalisées seul ou à « 4 mains », et de ses instruments de musique. » (virgules ajoutées)
   - « Pour vous accueillir, un petit temps de préparation est nécessaire : contactez-nous pour convenir ensemble de ce doux moment. » (au lieu de « nous vous invitons à nous contacter… »)
   - Ligne pratique : « Saint-Paul-de-Vern, Lot · juin à octobre · sur rendez-vous ».

## Contact

6. **E-mail affiché en clair.** `artelier-samonteil@orange.fr` est affiché et cliquable. Il risque de recevoir du spam. Faut-il le garder visible, ou ne laisser que le formulaire et les téléphones ?
7. **Ordre des téléphones.** Quel numéro mettre en premier : 06 85 81 31 48 ou 06 78 38 78 57 ? À qui correspond chacun ?
8. **Texte d'introduction** (corrigé, à relire) : « Pour une visite personnalisée et en musique « live » ou pour de plus amples renseignements, laissez-nous vos coordonnées ou appelez l'un des numéros indiqués. Nous nous ferons un plaisir de vous répondre. À bientôt. »
9. **Formulaire.** À quelle adresse les messages doivent-ils arriver ? Le service d'envoi est à choisir pour le site Astro.
10. **Politique de confidentialité.** Elle reste à rédiger : finalité, durée de conservation des messages, droits d'accès et de suppression. Le lien du formulaire pointe vers cette future page.
11. **Carte et itinéraire.** La carte et le lien « Voir l'itinéraire » utilisent les coordonnées GPS 44.8452653, 1.9399870 et non l'adresse. Le repère est-il bien placé sur l'ART'elier ?

## Œuvres et collections

Points ouverts sur les données du futur site Astro (20/11/2026). Chaque valeur provisoire porte le commentaire `# à confirmer` dans son fichier `site/src/content/…`.

12. **Dimensions corrigées.** Le nom du fichier photo et la fiche du site actuel se contredisent. La valeur retenue est celle de la fiche :
    - 22CM0205 (Miroirs d'Énigme) : 41 × 34 × **4,5** cm. Le fichier indique « 45 ».
    - 23CM0408 (Gardiens de la Terre) : 75 × 25 × **4,8** cm. Le fichier indique « 48 ».
    - 21DM0305 (Collection Privée) : 110 × 40 × **2,5** cm. Le fichier indique « 25 ».

    Ces valeurs sont-elles justes ?
13. **Forme ronde ou non.** Ces œuvres sont affichées comme rondes (diamètre × épaisseur) :
    - 19MBD0111 (Miroirs d'Énigme) : **Ø 43 × 5,5 cm**. La fiche indique « 43 x 5,5 cm » sans Ø, et le fichier « 43 x 55 ».
    - 22TM0112 (Miroirs d'Énigme) : **Ø 32 × 3 cm**. La fiche indique « 32 x 3 cm » sans Ø.
    - 23CM0307 (Collection Privée) : **Ø 20 × 3 cm**. La fiche indique « 20 x 3 cm » sans Ø.

    Ces trois œuvres sont-elles bien rondes ?
14. **23FM0112 (Collection Privée).** La fiche indique « Ø 36 x 34 x 3 cm ». Le site l'affiche pour l'instant en **36 × 34 × 3 cm**, sans Ø. L'œuvre est-elle ovale ? Si oui, quelles sont ses deux dimensions et son épaisseur ?
15. **22FM0407.** Elle figure à la fois dans les Miroirs d'Énigme et dans la Collection Privée. Le nouveau site la range dans les Miroirs d'Énigme uniquement. Est-ce juste ?
16. **Découpage des textes en strophes.** Le site actuel montre les retours à la ligne mais pas les strophes. Les découpages suivants restent à confirmer :
    - Les Arcs-en-ciel Noirs : le dernier vers « Sous le noir vibrent tous nos arcs-en-ciel. » forme-t-il une strophe à part ?
    - Les Gardiens de la Terre : texte découpé en 3 strophes, une par phrase.
17. **Bandeaux des collections.** Seuls les Miroirs d'Énigme ont un bandeau propre. Les Arcs-en-ciel Noirs, les Gardiens de la Terre et la Collection Privée reprennent pour l'instant le bandeau de la page Collections. Avez-vous une photo pour chacune ?
18. **Photos en petite définition.** La photo principale de 21DM0305 ne fait que 853 × 1280 px, et celles de 19MBD0111, 20SFM0112 et 19MBDF0212 font 1920 px de large. Le zoom de la lightbox sera donc limité pour ces œuvres. Existe-t-il des originaux plus grands ?
