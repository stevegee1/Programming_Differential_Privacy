Differential Privacy is a property of algorithm and not a property of
data as opposed to techniques like k-anonymity

It is important to know that two datasets are considered neighbours if
they differ in the data of a single individual. A function which
satisfies differential privacy is often called a mechanism.

Pr\[M(D)∈S\] ≤ e\^ε Pr\[M(D′)∈S\] - M: This is the algorithm or function
that releases some output based on your dataset

-   Neighboring datasets D and D': These are identical except for one
    person.

-   Possible sets of outputs S. Since M is random, it can output
    different values each run. epsilon is the scalar quantity that
    controls he closeness by ε (epsilon):

Small ε → strong privacy (outputs look almost identical whether or not a
person is included)

Large ε → weaker privacy Differential privacy makes it mathematically
impossible to tell, from the output, whether any single person's data
was used.

## My Research Gap

How should we set privacy budget to prevent bad outcomes in practice?
Nobody knows. The general consensus is that ε should be around 1 or
smaller, and values of above 10 probably don't do much to protect
privacy - but this rule of thumb could turn out to be very conservative.

## The Laplace Mechanism

We have the Laplace mechanism for differential privacy. When we query a
function f(D), we add Laplace noise to the output:

-   F(D)=f(D)+η, η ∼ Laplace(0,S)

Here, S = Δf/ϵ the scale of the noise, determined by the sensitivity of
the function Δf and the privacy budget ϵ.

The Laplace noise is centered around 0, meaning its mean is 0.

The noise can indeed be negative or positive; the absolute value is
bounded probabilistically (most values are near 0, but large deviations
are possible).

The PDF (probability density function):

f_Lap(x) = 1/(2S) exp(−\|x\|/S)

Shows the likelihood of different noise values for a fixed privacy
budget ϵ and sensitivity Δf.

The PDF is used mainly for analysis, visualization, and proofs, not to
directly generate the noise.

When we sample from this PDF, we get the actual η that we add to the
function output to produce a differentially private result.

### Key intuition

Scale S controls spread: larger S → more noise → stronger privacy, less
accuracy.

Center at 0: noise is unbiased; it shifts outputs up or down around the
true value.

PDF: tells us how likely each noise value is, so we understand the
distribution of outputs.

Sampling: actual DP mechanism uses a random sample η from this PDF; each
query produces a different η.

### Noise (η)

In the Laplace mechanism, the noise is drawn from a Laplace distribution
centered at 0.

This means it can be positive or negative.

Its magnitude is more likely to be small (near 0), but larger deviations
are possible --- that's the probabilistic part.

Adding this noise hides the effect of a single record, which is what
gives differential privacy.

### Privacy budget (ϵ)

ϵ is always a positive number; it is not noise, it is a parameter
controlling privacy.

Intuition: smaller ϵ → stronger privacy (more noise), larger ϵ → weaker
privacy (less noise).

ϵ is never negative, because the privacy guarantee is expressed as a
multiplicative bound e on probabilities --- negative ϵ would not make
sense mathematically.

### How they relate

Noise η ∼ Lap(0, S), with S = Δf / ϵ

Smaller ϵ → larger S → more spread → more privacy

Noise can go negative or positive, but ϵ is fixed for the mechanism

**Analogy:**

ϵ = "how tight the privacy leash is"

η = "how much wiggle room each output gets to hide individual data"

This variability is expected and is a natural consequence of
differential privacy, which depends on randomness to provide protection.

The underlying behavior of the algorithm should remain consistent, even
if the exact numbers vary. If you need to replicate results exactly (for
testing or debugging), you can set a fixed seed using tools like
np.random.seed() or random.seed() in Python.

For instructional purposes, however, we choose not to fix seeds so that
the examples reflect the true behavior of private algorithms in
practice.

## Conclusion

**What is the unit of privacy?**

The typical definition of DP defines neighboring datasets as any two
datasets that differ in "one person's data." The unit of privacy refers
to the formal definition of "neighboring" used in a differential privacy
guarantee. The most common unit of privacy is *one person* --- meaning
the privacy guarantee protects the whole person, forever. This is also
commonly referred to as *user-level privacy*.

-   Each individual's data is contained in exactly one row of the data.
-   It's best to avoid using a different unit of privacy whenever
    possible.

Under the "one person = one row" simplification, neighboring datasets
differ in one row.

### What does "differ" mean?

**Substitution Adjacency:**\
Two datasets are considered neighbors if x' can be obtained by changing
a row in x. The sizes of x and x' are equal.

**Add-Remove adjacency:**\
Two datasets are considered neighbors if x' can be obtained by adding a
row to x. The sizes of x and x' are different (by one row).
