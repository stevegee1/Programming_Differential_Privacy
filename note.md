# Chapter 1 - 3
## Data Privacy vs Security
A clear distinction between both concepts is that data privacy is concerned
about releasing information and controlling what can be learnt from that
information. While security (like encryption techniques) prevents unauthorised
access to information.

## De-identification
De-identification is the process of removing identifying information from a dataset

**The pitfall of de-identification**: There is no inherent difference between a benign query and that of a malicious.
This is why adhoc approaches to privacy fails. They rely on implicit assumptions
about how the data wlll be used and who is asking the questions.

## Differential Privacy
**Differential Privacy** was designed to address these challenges. It provides
formal guarantees that hold regardless of what queries are asked or what
auxiliary information the adversary possesses.
