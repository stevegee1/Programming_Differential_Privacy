# K-ANONYMITY

K-Anonymity is a formal privacy definition. It assumes that an adversary has access to auxiliary information (quasi-identifiers). The goal is to ensure that the adversary can learn information only about a group of at least k individuals, not about any single individual.

My understanding is this: when we consider a subset of columns in a dataset (the quasi-identifiers), any information identifiable from these attributes should be shared by at least k rows. You can narrow down to a group of size ≥ k, but not to any specific member inside that group.

## Formal Definition

A dataset D satisfies k-Anonymity for a given k if:

For each row r₁ ∈ D, there exist at least k − 1 other rows r₂, …, r_k ∈ D such that:

Π_qi(D)_{r₁} = Π_qi(D)_{r₂} = … = Π_qi(D)_{r_k}

where qi(D) is the set of quasi-identifier attributes, and Π_qi(D)_r denotes the projection of row r onto those attributes.

The quasi-identifier set is assumed to be fixed a priori—selected before anonymization. This matches the attacker model: we assume the adversary knows and uses these attributes for linkage attacks.

## Checking for k-Anonymity

Consider this dataset:

```
age   preTestScore   postTestScore
42    4              25
52    24             94
36    31             57
24    2              62
73    3              70
```

### Why does this dataset fail k-Anonymity for any k > 1?

None of the rows share the same quasi-identifiers (age, preTestScore, postTestScore).
Therefore, no row has the required duplicates.

- For k = 2 → fails
- For k = 3, 4, 5 → impossible

### Why does it trivially satisfy k = 1?

Because every row is identical to itself.

k = 1 requires each row to have at least one matching record (itself), which is always true.

**Summary:**
The dataset fails k-Anonymity for any k > 1 because all rows are unique on the quasi-identifiers.

## Optimal Generalization

Finding the optimal generalization that satisfies k-Anonymity while maximizing utility is NP-hard.

## Removing Outliers (Clipping)

Clipping quasi-identifiers to lie within a specified range removes outliers.
This may reduce utility but often helps the dataset form larger, more uniform groups.

### Clipping vs Bucketing

- **Clipping:** Truncates extreme values (e.g., capping ages at 90).
- **Bucketing:** Groups values into ranges (e.g., age 20–29).

## The Homogeneity Attack

k-Anonymity protects identity disclosure, but not attribute disclosure.

This attack occurs when:

1. The quasi-identifiers are similar enough to form groups.
2. All rows in a group share the same sensitive attribute.

### Example

Group G after generalization:

```
Age = 20–29
ZIP = 123**
Disease = HIV for all members
```

If you know someone belongs to G, you know their disease—without identifying their exact row.

## Background Knowledge & Linkage Attacks

Suppose the quasi-identifiers used are only:

- Age (generalized)
- ZIP (generalized)

But gender remains un-generalized.

Group:

```
F, M, M, M
```

If the attacker knows the target is female, they identify the row exactly—breaking anonymity.

## Limitations of k-Anonymity

k-Anonymity ensures indistinguishability on quasi-identifiers, but:

- It does not ensure diversity of sensitive attributes.
- It does not protect against strong auxiliary information.
- High-dimensional data becomes difficult to anonymize effectively.

This led to stronger models:

- **ℓ-Diversity**
- **t-Closeness**
- **Differential Privacy**
