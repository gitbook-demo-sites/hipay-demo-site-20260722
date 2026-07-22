---
description: "Dans ce document, nous decrivons la methode pour activer et utiliser le module Hipay pour Prestashop. Nous listons egalement les differents points de "
icon: file-lines
---

# PrestaShop Professional

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/uncategorized/prestashop-professional](https://developer.hipay.com/uncategorized/prestashop-professional)
{% endhint %}

Dans ce document, nous decrivons la methode pour activer et utiliser le module Hipay pour Prestashop. Nous listons egalement les differents points de blocages qui peuvent survenir ainsi que leurs solutions.

* Le module Hipay est present en natif sur le CMS Prestashop. Il n'est donc pas necessaire de le telecharger a part, il suffit de l'activer sur votre backoffice Prestashop, dans la rubrique Modules

* Il est possible de telecharger le module en cas de reinstallation ou de mise a jour a cette adresse : http://addons.prestashop.com/en/payments-gateways-prestashop-modules/1746-hipay.html

* Le module gere uniquement le paiement a l'acte. Hipay propose egalement un service d'abonnement, il faut dans ce cas nous contacter afin que l'on vous fournisse la documentation technique pour le developper.

* Si vous souhaitez configurer plusieurs devises, vous devez ouvrir autant de sous-compte sur votre compte Hipay. Pour cela, cliquez sur Synthese des comptes et Creer un compte secondaire . Remplissez le formulaire et choisissez la devise desiree. Attention : il faut inscrire votre site sur chaque sous-compte.

* Le module gere notre plateforme de production ainsi que la plateforme de test.

## Pre-requis

Inscription d'un compte marchand

Pour utiliser Hipay, vous avez besoin de posseder un compte marchand. C'est un processus simple qui se fait directement en ligne. Rendez vous sur https://www.hipaydirect.com/registration/register , puis suivez les instructions. Une fois que vous aurez cree votre compte Hipay, vous recevrez une confirmation par email avec les instructions pour finaliser votre inscription.

Apres avoir finalise votre inscription, vous pourrez vous connecter sur votre compte via l'url suivante : https://professional.hipay.com/
Inscription de votre site internet

Inscrivez votre site internet dans votre compte marchand

Les informations demandees sont utilises pour distinguer les differents sites internet enregistres dans votre compte.

Entrez le nom de votre site, l'URL, le theme principal et secondaire,le mot de passe marchand, l'email de contact et le telephone (optionnel).

## Installation et configuration

Configuration du compte

Une fois votre site inscrit, rendez-vous sur votre backoffice Prestashop. Cliquez sur Modules et sur Paiement . Au niveau du module Hipay,cliquez sur Installer :

Cliquez ensuite sur Configurer

Vous devrez alors renseigner les identifiants API que vous trouverez sur votre compte prealableblement cree sur le Backoffice HiPay. Vous trouverez vos identifiants en cliquant sur l'onglet Compte > Informations > Identifiants API

## Configuration du compte de test

Si vous le souhaitez, il est possible de creer et configurer un compte de test. Pour cela il est necessaire de se rendre sur le BO de test a l'adresse suivante : https://test-www.hipaydirect.com/registration/register Vous devrez alors creer un compte de la meme maniere que le compte de production, puis renseigner les identifiants en cliquant sur le bouton CONNECTER LE COMPTE DE TEST. Vous pourrez alors switcherentre le compte de production et le compte de test.

## Paiement

### Type de paiement

Vous avez ici le choix entre le paiement en Redirection (page hebergee) ou en Iframe (sur votre site).

* Avec option Redirection, lorsque l'utilisateur clique sur le bouton payer, il est redirige vers la page de paiement HiPay. Une fois la transaction terminee, l'utilisateur est redirige vers votre magasin.

* Avec option Iframe, lorsque l'utilisateur clique sur le bouton payer, le formulaire de paiement s'affiche dans une iFrame. Cela signifie que l'utilisateur ne quitte pas votre magasin.

### Type de capture

Vous avez le choix entre plusieurs mode de capture pour les commandes recues.

* Avec le mode de capture automatique, votre client sera immediatement facture / debite une fois l'achat effectue.

* Avec le mode de capture manuelle, votre client ne sera pas debite immediatement. Au lieu de cela, une autorisation sera faite, vous permettant de confirmer le debit plus tard. Par exemple, ce mode est approprie lorsque vous souhaitez facturer votre client uniquement lorsque les articles ont ete expedies.

### Bouton de paiement

Choisissez le bouton de paiement que vous souhaitez voir apparaitre sur votre page de commande et cliquez sur Enregistrer les modifications . Vous pouvez egalement choisir un bouton de paiement personnalise mais celui-ci doit restecter les dimentions autorisees (400px x 400px et 300 Ko maximum).

Points de blocages
Configuration du compte

Impossible de recuperer les categories Hipay. Merci de vous referer a votre journal des erreurs pour plus de details.

Verifiez votre id site, le systeme ne le reconnait ou ne le trouve pas.

Les categories Hipay ne sont pas definies pour chaque ID de site.

Vous n'avez pas selectionne la categorie pour le compte dans le menu deroulant.
Lors du paiement

Il y a 1 erreur :[Hipay] MerchantAccount or merchantUserSpace does not exist or disabled - Invalid login value : 0000000 errorMerchantAccount or merchantUserSpace does not exist or disabled - Invalid login value : 0000000 )

Verifiez votre id compte, le systeme ne le reconnait ou ne le trouve pas.\ Si l'identifiant est correcte, contactez notre service client a [email protected] pour connaitre la raison de sa desactivation.

[Hipay] Invalid orderCategory value : 000 errorInvalid orderCategory value : 000 )

L'id de la categorie selectionne n'est pas correcte. Peut arriver suite a une modification des categories sur votre compte Hipay. Recommencez la configuration sur votre backoffice Prestashop pour obtenir ou renouveler les categories. Si deux categories Autres apparaissent, choisissez la deuxieme et validez.

[Hipay] Invalid merchant website password ! ( error Invalid merchant website password ! )

Le mot de passe marchand que vous avez indique n'est pas correct. Le mot de passe marchand est le mot de passe que vous avez choisi lors de l'inscription de votre site.\ Si vous l'avez oublie, vous pouvez le renouveler en vous connectant sur votre compte Hipay, en cliquant sur Creation de bouton et Editer a cote de votre site.

Le paiement par Hipay n'est pas propose sur la page de paiement ?

Suivez cette manipulation :\ Configurez vos informations de connexion sur le module, validez, retournez sur la liste des modules et reinitialisez le module Hipay, retournez sur la configuration du module, definissez les zones et validez. Le paiement par Hipay devrait etre propose.

## Support

En cas de question concernant les reversements et votre contrat, envoyez un email a [email protected]

En cas de question technique, contactez notre support technique a [email protected]
