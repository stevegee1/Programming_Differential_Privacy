## Global Sensitivity
GS(f) = max |f(x) - f(x')|. Where d(x,x') <= 1
x and x' are two neighboring datasets.
The measure of sensitivity is called "global" because it is independent of the
actual dataset being queried (it holds for any choice of neighboring x and x').

### Symmetric Difference
d(x, x') = |(x - x') U (x' - x)

- If x' is constructed from x by adding one row, then d(x,x') = 1
- if x' is constructed from x by remeving one row, then d(x, x') = 1
- if x' is constructed from x by modifying one row, then d(x, x') = 2
This particular definition of distance results in what is typically called unbounded differential privacy. Many other definitions are possible, including one called bounded differential privacy in which modifying a single row in a dataset does
result in a neighboring dataset.

### Calculating Sensitivity
For some simple functions on real numbers, the answer is obvious:
The global sensitivity of 𝑓(𝑥) = 𝑥 + 𝑥 is 2, since changing 𝑥 by 1 changes 𝑓(𝑥) by 2
• The global sensitivity of 𝑓(𝑥) = 5 ∗ 𝑥 is 5, since changing 𝑥 by 1 changes 𝑓(𝑥) by 5
• The global sensitivity of 𝑓(𝑥) = 𝑥 ∗ 𝑥 is unbounded, since the change in
𝑓(𝑥) depends on the value of 𝑥

**Counting queries** always have a sensitivity of 1
**Summation queries** sum up the attribute values of dataset rows. Sensitivity
for these queries is not as simple as it is for counting queries. Adding a new
row to the dataset will increase the result of our example query by the age of
the new person. That means the sensitivity of the query depends on the contents
of the row we add.
As a rule of thumb, summation queries have unbounded sensitivity when no lower
and upper bounds exist on the value of the attribute being summed. When lower
and upper bounds do exist, the sensitivity of a summation query is equal to the
difference between them.
**Average queries** The easiest way to answer an average query with differential
privacy is by re-phrasing it as two queries: a summation query divided by a
counting query.

Unbounded sensitivity cannot be directly answered with differential privacy
using the Laplace mechanism. we can often transform such queries into equivalent
queries with bounded sensitivity, via a process called clipping.


### Clipping
Queries with unbounded sensitivity cannot be directly answered with differential
privacy using the Laplace mechanism. We can often transform such queries using Clipping

