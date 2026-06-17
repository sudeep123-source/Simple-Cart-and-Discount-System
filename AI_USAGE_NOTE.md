# AI Tool Usage Note

**Tool used:** Claude (Anthropic), used as a pair-programming assistant
throughout development.

**How it helped:** I described the requirements (add items to cart,
calculate total, apply a discount, display final amount, built in Python) and
Claude generated an initial working version of the application, structured
around a `Cart` class, an `Item` model, and a discount-lookup function. From
there, I used Claude iteratively to harden the code: adding input validation
for edge cases (empty item names, negative prices, zero quantities, invalid
discount codes), preventing a fixed discount from pushing the total below
zero, and improving the CLI flow so invalid input prompts the user to retry
instead of crashing or silently failing. Claude also ran the code after each
change to verify behavior (e.g., testing that an invalid discount code is
rejected, that a $100 fixed discount on a $10 cart correctly caps at $0
instead of going negative) before the final version was finalized, which
sped up the verification cycle significantly compared to manually tracing
through test cases by hand.

**Challenges encountered:** The main challenge was deciding how strict
validation should be without making the CLI tedious to use — for example,
deciding whether an invalid discount code should immediately fall back to "no
discount" or let the user retry (I chose the latter for a better user
experience). Another small challenge was handling the edge case where a
flat-amount discount code exceeds the cart's total; this was resolved by
capping the discount at the cart total so the final amount never goes
negative. Overall, AI assistance was most useful for quickly iterating on
validation logic and catching edge cases I might have initially overlooked,
while I focused on reviewing the logic, defining requirements, and deciding
on the final UX behavior.
