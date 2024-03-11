
# Livraison avec des vehicle 

## Modélisation

### Données

- Données du véhicules
  - **distance maximal** `max_dist`
  - **capacité** `capacity`
  - **charge rapide** `charge_fast`
  - **charge moyenne** `charge_medium`
  - **charge lente** `charge_slow`
  - **heure de début** `start_time`
  - **heure de fin** `end_time`
- Nombre de camion `nb_cam`
- Donnée de visite `v`
  - **Identifiant de la visite** `visit_id`
  - **Nom de la visite** `visit_name`
  - **Emplacement de la visite** 
    - (latitude) `visit_lat`
    - (longitude) `visit_lon`
  - **Quantité de sac à livrer par visite** `demand`
  - **est dépôt** `est_dépot` = 0 si visite = 1 si dépôt
- Distance entre les visite `dist_visit[v1][v2]`
- Temps entre les visite `temp_visit[v1][v2]`

### Constante

- Durée d'une livraison : `10sec*sac+5min`
- Durée de chargement de sac au dépôt : `10 minute`

### Variable de décision

Chaque élément de E et représenter de la façon suivante:

```typescript
interface {
    idVisite: number;
    chargement: boolean;
    rechargement: boolean;
}
```

On considère ajoute les retours dépôt dans les vites

E  Ensembles des visites ordonnée pour un camion C 
$$
E(c): \{\}
$$

### Contrainte

- somme des distance parcouru sans recharger ne doit pas dépasser la distance maximal (`max_dist`) du véhicule à aucun moment
- somme des quantité de sac à livrer par visite (somme des `demand`) sans recharger des sacs ne doit pas dépasser la capacité maximal (`capacity`) du véhicule à aucun moment
- temps total de la tourné <= HeurFin-HeureDébut
  - pour chaque visite tempsTotal += temps de trajet précent + nbsac*10sec+5min
  - si dépot 
    - Si recharge temps total += temps de recharge + temps trajet précédent
    - Si chargement tempstotal += 10minutes + temps trajet précédent
- On ne passe qu'une seul fois chez un client avec un seul camion 
- Livrer toutes les commandes

### Objectif

* Minimiser le nombre de camion
* Minimiser le nombre km parcouru par camion
* Minimiser l'agrégations des deux percement objectif

### Comment représenter une solution en programmation ?

```ts
interface Solution{
	idSite: number;
    chargement: boolean;
    rechargement: boolean;
}

type Solutions = solution[]

type AllSolutions = Solutions[] = solution[][]

```

Nos solution se représenter sous la forme d'objet

L'objet Solutions et un tableau ordonnée contenant les identifiant du site ainsi que si on charge ou non le camion et si l'on recharge ou non le camion.



### Comment évaluer si une solution est réalisable ou non réalisable ?

Cela dépendra de notre implémentation.

Si on a contraint la génération des solution à être réalisable dans ce cas il n'est pas nécessaire d'évaluer si la solution est réalisable. Cependant l'évaluation de la solution se fera via l'agrégation de nos différents objectifs.

Si on ne contraint pas la génération des solution à être réalisable dans ce cas il est nécessaire d'ajouter à notre agrégat d'objectif un facteur de réalisabilité.

### Proposition d'instance sans non réalisable

#### Instance non réalisable

##### Distance trop élever

La contrainte de chargement de la batterie n'est pas réalisable et livrer toutes les commandes

Matrice de ditance

|       | **A** | **B** |
| ----- | ----- | ----- |
| **A** | 0     | 200   |
| **B** | 200   | 0     |

Données du véhicules

- `max_dist`=120

#### Quantité de sac à livrer

La contrainte de capacité maximal n'est pas réaliser  et la contrainte de livraison unique n'est pas respecter non plus et livrer toutes les commandes

Données des visites

| Id   | Nom  | Demande |
| ---- | ---- | ------- |
| 1    | V1   | 150     |

Données du véhicules

- `capacity`=100

#### Temps de livraison

La contrainte du temps de liveraison n'est pas réspecter et livrer toutes les commandes

Matrice de temps

|       | **A** | **B** |
| ----- | ----- | ----- |
| **A** | 0     | 5     |
| **B** | 5     | 0     |

Données du véhicules

- `start_time` = 10:00
- `end_time` = 14:00
