## Sequential Composition

This property deals with the additive law of running differential privacy mechanisms on the same input data. It provides a total bound on the privacy cost.

### Theorem 1 (Sequential Composition)

Let:
- \(F_1(X)\) satisfy \(\epsilon_1\)-differential privacy,
- \(F_2(X)\) satisfy \(\epsilon_2\)-differential privacy.

Then the mechanism \(G(X)\) which releases both results \((F_1(X), F_2(X))\) satisfies \((\epsilon_1 + \epsilon_2)\)-differential privacy.


The bound on privacy cost given by sequential composition is an **upper bound** — the actual privacy cost of two particular differentially private releases may be smaller than this, but never larger. This is a theoretical bound.

## Parallel Composition

Parallel composition is based on the idea of splitting your dataset into
disjoint chunks and running a differentially private mechanism on each
chunk separately. Since the chunks are disjoint, each individual's data
appears exactly in one chunk. If F(x) satisfies e-differential privacy
And we split X into disjoint chunks such that x1 U x2 U... U Xn = X and
x1 n x2 n ... n xn = {} Then we can say running differentially private
mechanism on each disjoint satisfies e-differntial privacy.

### Histogram

Histograms are particularly interesting for differential privacy because
they automatically satisfy parallel composition. Histogram splits
dataset into "bins" baseed on the value of one of the data attributes,
and counts the number rows in each bin.

### Contingency Tables

Another name is crosstab. It counts the frequency rows in a dataset with
particular values for more than an attribute at a time. Contingency
tables are used to show relationship between two variables when
analyzing data.

As we split the dataset further into disjoint chunks, each chunk has
fewer rows in it, so all of the counts get smaller. If we think of
things in terms of signal and noise, a large count represents a strong
signal. This is unlikely to be disrupted too much by relatively weak
noise, and therefore the results are likely to be useful after the noise
is added. However, a small count represents a weak signal which might be
significantly disturbed ater the noise is added.

So while it may seem that parallel composition gives us something "for
free" (more results for the same privacy cost), that's not really the
case. Parallel composition simply moves the tradeoff between accuracy
and privacy along a different axis - as we split the dataset into more
chunks and release more results, each result contains a weaker signal,
and so it's less accurate.

#### Post Processing

It is impossible to reverse the privacy protection provided by
differential privacy by post-processing the data in some way. The
post-processing property means that it's always safe to perform
arbitrary computations on the output of a differentially private
mechanism - there's no danger of reversing the privacy protection the
mechanism has provided. It's fine to perform post-processing that might
reduce the noise or improve the signal in the mechanism's output. In
fact, many sophisticated differentially private algorithms make use of
post-processing to reduce noise and improve the accuracy of their
results.

A function might contain auxiliary information about elements of the
dataset, and attempt to perform a linkage attack using this information.
The post-processing property says that such an attack is limited in its
effectiveness by the privacy parameter, regardless of the auxiliary
information contained.
