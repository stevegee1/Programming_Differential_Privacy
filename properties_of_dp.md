## Sequential Composition

This property deals with the additive law of running differential privacy mechanisms on the same input data. It provides a total bound on the privacy cost.

### Theorem 1 (Sequential Composition)

Let:
- \(F_1(X)\) satisfy \(\epsilon_1\)-differential privacy,
- \(F_2(X)\) satisfy \(\epsilon_2\)-differential privacy.

Then the mechanism \(G(X)\) which releases both results \((F_1(X), F_2(X))\) satisfies \((\epsilon_1 + \epsilon_2)\)-differential privacy.


The bound on privacy cost given by sequential composition is an **upper bound** — the actual privacy cost of two particular differentially private releases may be smaller than this, but never larger. This is a theoretical bound.



