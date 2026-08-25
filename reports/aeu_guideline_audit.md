# AEÜ – International Journal of Electronics and Communications
## Audit du guide des auteurs et premier brouillon de conversion

**Statut :** préparation non compilée. Aucun fichier `.tex` ou `.bib` AEÜ final n’est généré à ce stade, conformément à la demande de validation de l’auteur.

## 1. Adéquation scientifique au journal

L’AEÜ publie des travaux originaux sur les dispositifs électroniques, les circuits et les systèmes de communication. Son périmètre inclut explicitement les systèmes d’antennes, les systèmes micro-ondes, les circuits RF et la réalisation de systèmes de communication. Le manuscrit est donc pertinent s’il est présenté comme une contribution de conception et de validation électromagnétique d’une antenne patch THz compacte, avec un accent sur la suppression des ondes de surface par substrat PBG, l’adaptation d’impédance, le gain, l’efficacité et les applications de communication THz.

Le design est actuellement un travail de simulation. Il ne faut pas présenter une fabrication, une mesure expérimentale ou une validation en laboratoire comme déjà réalisée. La formulation recommandée est « full-wave simulated », « numerically evaluated » et « cross-validated using CST and HFSS ».

## 2. Type d’article et limite de longueur

Le guide prévoit deux catégories principales : Research Paper jusqu’à 20 pages, toutes composantes incluses, et Short Communication jusqu’à 10 pages. Le manuscrit complet est clairement plus adapté à **Research Paper**. La version de conversion devra respecter la limite totale de 20 pages, comprenant texte, figures, tableaux et références. La version AGU actuelle de 25 pages ne peut donc pas être transférée telle quelle.

## 3. Format de soumission et modèle

Le guide demande des fichiers sources éditables et accepte LaTeX. Elsevier recommande le modèle CAS disponible dans `els-cas-templates.zip`. Le modèle `cas-dc.cls` est le choix initial le plus pratique pour une soumission LaTeX en double colonne. Toutefois, le guide AEÜ demande pour la version de revue : 12 pt, marges de 1 pouce, une colonne et interligne double. La mise en page de revue doit donc être distinguée de la mise en page finale : le premier brouillon doit privilégier la conformité de soumission, et non reproduire automatiquement le deux-colonnes Wiley.

Le PDF n’est pas un fichier source acceptable. Il faudra fournir au moment de la soumission le `.tex`, le `.bib` et toutes les figures éditables. Le PDF sert uniquement à la lecture et au contrôle.

## 4. Structure requise et recommandée

La page de titre doit contenir un titre concis sans abréviation non nécessaire, les noms complets dans le même ordre que dans le système de soumission, les affiliations complètes avec adresse postale et pays, ainsi que l’auteur correspondant et son adresse électronique.

L’abstract doit être autonome, factuel et inférieur ou égal à 250 mots. Il doit présenter le problème, la méthode, les résultats principaux et les conclusions, sans citation sauf nécessité absolue. Les mots-clés doivent être en anglais, entre 1 et 7 termes, et éviter les expressions trop longues ou les abréviations non établies.

Les highlights sont fortement recommandés et doivent être fournis dans un fichier éditable séparé nommé avec le mot « highlights ». Ils doivent contenir 3 à 5 puces, chacune de 85 caractères maximum, espaces compris. Un graphical abstract est recommandé mais facultatif ; ses dimensions recommandées sont 531 × 1328 pixels, hauteur × largeur, ou une proportion équivalente, et il doit être soumis séparément.

Le corps doit utiliser des sections numérotées et des sous-sections numérotées sous la forme 1, 1.1, 1.1.1. Les références croisées doivent mentionner les numéros des sections, tableaux et figures. Les équations doivent être du texte éditable, numérotées consécutivement et écrites avec les unités SI. Les tables doivent être éditables, citées dans le texte, numérotées dans l’ordre d’apparition, accompagnées d’une légende et sans règles verticales ni ombrage inutile. Les figures doivent être citées, numérotées dans l’ordre, fournies séparément avec une convention de nommage logique et accompagnées d’une légende complète.

L’ordre de travail recommandé est : Introduction, Antenna Design and Methodology, Results and Discussion, Conclusion, Acknowledgements, declarations and data statement as requested by the submission system, References, Tables and Figures when submitted as separate files. La section exacte de déclarations doit être vérifiée au moment du dépôt dans Editorial Manager.

## 5. Citations et références

L’AEÜ exige des références numériques entre crochets dans le texte, par exemple « as demonstrated [3,6] » ou « Smith et al. [8] ». La liste bibliographique doit suivre l’ordre d’apparition dans le texte, et non l’ordre alphabétique AGU. Les DOI sont fortement recommandés. Les noms des revues doivent être abrégés selon la List of Title Word Abbreviations (LTWA). Pour plus de six auteurs, les six premiers doivent être indiqués, suivis de « et al. ». Les pages finales doivent utiliser la forme abrégée lorsque le style l’exige.

La base nettoyée de 29 références du projet MOTL est une base de départ, mais elle devra être convertie au style numérique Elsevier et contrôlée une nouvelle fois après l’ajout des références AEÜ. Toute référence ajoutée doit être réellement citée et soutenir une phrase précise ; il ne faut pas ajouter des références uniquement pour augmenter l’auto-citation du journal.

## 6. Données, éthique, financement et IA

Pour l’AEÜ, les instructions de données imposent l’Option C : déposer les données dans un dépôt pertinent et les citer/lier, ou expliquer pourquoi elles ne peuvent pas être partagées. Pour ce travail de simulation, le meilleur choix est un dépôt public comprenant les dimensions, paramètres matériaux, fichiers de résultats numériques et données des figures, avec DOI Zenodo si possible.

Le financement doit être déclaré. Si aucun financement spécifique n’a été reçu, la phrase recommandée est : « This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. » La déclaration de conflits doit être saisie dans l’outil Elsevier ; en l’absence de conflit, sélectionner « I have nothing to declare » et utiliser une déclaration cohérente dans le manuscrit.

Elsevier exige une déclaration de l’utilisation d’outils d’IA générative dans la préparation du manuscrit. La déclaration doit être placée dans une nouvelle section avant les références. Pour ce projet, la formulation devra mentionner l’assistance utilisée pour l’anglais, l’organisation de passages, le support LaTeX, la cohérence bibliographique et la lettre d’accompagnement, tout en précisant qu’aucune donnée de simulation, figure, valeur numérique, modèle CST/HFSS ou conclusion scientifique n’a été généré ou modifié par l’IA.

## 7. Figures et résolution

Les dessins vectoriels doivent être fournis en EPS ou PDF avec polices incorporées ou texte converti en éléments graphiques. Les images en couleur ou niveaux de gris doivent généralement atteindre au moins 300 dpi ; les dessins bitmap au moins 1000 dpi ; les combinaisons ligne/halftone au moins 500 dpi. Les fichiers doivent être séparés et logiquement nommés. Les figures comprenant plusieurs panneaux doivent rester accessibles et leurs symboles et abréviations doivent être expliqués dans les légendes.

Les figures EPS et PNG du projet devront être contrôlées individuellement pour la résolution, la lisibilité des axes, la taille des caractères et la cohérence des légendes. Les fichiers PDF produits automatiquement à partir des EPS doivent être conservés seulement s’ils sont nécessaires au modèle CAS.

## 8. Références AEÜ candidates à examiner

### Candidate 1: PBG/EBG and antenna arrays

Jafari, F. S., Zarrabi, F. S., and Ebrahimi, S. (2018). Fractal EBG structure for shielding and reducing the mutual coupling in microstrip patch antenna array. *AEU – International Journal of Electronics and Communications*. DOI: https://doi.org/10.1016/j.aeue.2018.06.028.

**Usage possible :** soutenir l’explication générale selon laquelle les structures EBG peuvent contrôler la propagation de surface et réduire le couplage dans des structures microstrip. **Limite :** l’article concerne une antenne réseau à 5.9 GHz et ne doit pas être présenté comme une validation directe du résultat THz proposé.

### Candidate 2: miniaturisation et charges métamatériaux

Varamini, G., Keshtkar, A., and Naser-Moghadasi, M. (2018). Miniaturization of microstrip loop antenna for wireless applications based on metamaterial metasurface. *AEU – International Journal of Electronics and Communications*, 83, 32–39. DOI: https://doi.org/10.1016/j.aeue.2017.08.024.

**Usage possible :** soutenir le contexte sur la miniaturisation, la redistribution du courant et l’utilisation de charges métamatériaux. **Limite :** l’article est principalement micro-onde et expérimental ; il ne doit pas être utilisé pour justifier directement les performances du patch THz PTFE.

### Candidate 3: article AEÜ à confirmer avant intégration

Varamini, G. et al. (2018). Compact and miniaturized microstrip antenna based on fractal and metamaterial loads with reconfigurable qualification. *AEU – International Journal of Electronics and Communications*. ScienceDirect PII: S1434841117315066.

**Statut :** pertinent pour la miniaturisation et les charges métamatériaux, mais les métadonnées complètes, le DOI, le volume et les pages doivent être vérifiés avant toute insertion dans le `.bib`. Ne pas l’ajouter au manuscrit tant que cette vérification n’est pas terminée.

### Références THz connexes, non AEÜ

Khezzar et al. (2021), « New design of a broadband PBG-based antenna for THz band applications », DOI 10.1016/j.photonics.2021.100947, est très proche scientifiquement mais publié dans *Photonics and Nanostructures – Fundamentals and Applications*, pas dans l’AEÜ. Il peut renforcer le benchmarking technique mais ne doit pas être présenté comme une référence AEÜ.

Temmar et al. (2020), « Enhanced Flexible Terahertz Microstrip Antenna Based on Modified Photonic Crystal », est également pertinent pour les substrats photoniques THz, mais il doit être cité avec ses métadonnées exactes après vérification et ne constitue pas une auto-citation AEÜ.

## 9. Premier plan de conversion sans génération de fichiers finaux

Le premier brouillon devra partir du dernier `main.tex` MOTL et conserver les sections scientifiques, les résultats CST/HFSS, les figures et les tableaux. Il devra remplacer le front matter Wiley par le front matter CAS Elsevier, convertir les citations numériques vers les commandes natbib du modèle CAS, adapter le titre et le résumé à la limite de 250 mots, écrire 3 à 5 highlights séparés de 85 caractères maximum, renuméroter les sections au format Elsevier et préparer une liste de références numérique dans l’ordre d’apparition.

Le benchmarking devra être réécrit afin de comparer explicitement les conditions expérimentales ou simulées : fréquence, bande passante, architecture simple ou réseau, substrat, alimentation, métrique de gain, efficacité et statut simulation/mesure. Les résultats supérieurs d’autres travaux devront être expliqués sans les traiter comme des comparaisons strictement équivalentes.

Aucun `.tex` ni `.bib` de conversion finale ne doit être généré avant validation des références candidates, du type d’article et de la stratégie de données. Le modèle CAS téléchargé est disponible dans `/home/ubuntu/aue_project/template/els-cas-templates/` pour la prochaine étape.

## 10. Validations demandées à l’auteur

1. Confirmer **Research Paper** plutôt que Short Communication.
2. Confirmer si les deux références AEÜ candidates doivent être intégrées dans l’Introduction et le benchmarking.
3. Confirmer que les données de simulation peuvent être déposées publiquement, ou indiquer quelles données ne peuvent pas être partagées.
4. Confirmer le titre anglais, les deux auteurs, les affiliations et l’adresse électronique correspondante.
5. Confirmer si un graphical abstract doit être préparé ; il est recommandé mais facultatif.
6. Confirmer si les biographies et photographies des auteurs demandées dans le guide doivent être préparées séparément.

## Sources officielles et vérifiées

- Guide officiel AEÜ : https://www.sciencedirect.com/journal/aeu-international-journal-of-electronics-and-communications/publish/guide-for-authors
- Page officielle du journal : https://www.sciencedirect.com/journal/aeu-international-journal-of-electronics-and-communications
- Modèle LaTeX CAS recommandé par Elsevier : https://assets.ctfassets.net/o78em1y1w4i4/5uFmLZJTPDMAUjFnHRpjj8/6f19a979146eb93263763d87a894ab0d/els-cas-templates.zip
- Jafari, Zarrabi, and Ebrahimi, article AEÜ sur la structure EBG : https://doi.org/10.1016/j.aeue.2018.06.028
- Varamini, Keshtkar, and Naser-Moghadasi, article AEÜ sur la miniaturisation par métasurface : https://doi.org/10.1016/j.aeue.2017.08.024
- Khezzar et al., article THz/PBG hors AEÜ, utilisé seulement pour le contexte technique : https://doi.org/10.1016/j.photonics.2021.100947

## Nouvelle référence AEÜ THz vérifiée

Alibakhshikenari, M., Virdee, B. S., Salekzamankhani, S., Babaeian, F., Ali, S. M., Iqbal, A., and Al-Hasan, M. (2023). On-chip terahertz antenna array based on amalgamation of metasurface-inspired and artificial magnetic conductor technologies for next generation of wireless electronic devices. *AEU – International Journal of Electronics and Communications*, 167, 154684. DOI: https://doi.org/10.1016/j.aeue.2023.154684.

La page officielle indique une antenne réseau on-chip 2 × 24, fabriquée sur une plaquette de silicium de 35 µm, avec un gain moyen mesuré de 20.36 dBi et une efficacité de rayonnement de 37.5% sur 0.3–0.314 THz. Cette référence est pertinente pour le benchmarking THz, mais elle doit être séparée de la comparaison directe : son architecture est un grand réseau on-chip MTS/AMC fabriqué et mesuré, alors que le présent travail est une antenne patch unique PBG sur PTFE évaluée par simulation. Elle peut être ajoutée dans l’Introduction et dans le paragraphe de benchmarking avec cette limitation explicitement formulée.
