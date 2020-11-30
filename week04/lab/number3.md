3. Design an algorithm using pseudocode and flowchart for the following scenario:

A computer supplies called True Disk has set up accounts for countless businesses in the Klang Valley. True Disk sends out invoices monthly and will give discounts if payments are made within 10 days. The discounting policy is as follows:

If the amount of the order for the computer supplies is greater than $1000, subtract 4% for the order; if the amount is between $500 and $1000, subtract a 2% discount, if the amount is less than $500, do not apply any discount.

```psuedocode
BEGIN
    PRINT "Enter number of days taken to make payment"
    READ days
    PRINT "Eneter the amount of order"
    READ amount
    discount = 0

    IF(days =< 10) THEN
        IF(amount > 1000) THEN
            discount = 4
        ELSE
            IF((amount >= 500) AND (amount =< 1000)) THEN
                discount = 2
            ENDIF
        ENDIF

        discountedAmount = amount - (amount * discount/100)
        PRINT "The discounted amount is:", discountedAmount
    ELSE
        PRINT "no dicounting policy"
    ENDIF
END
```
![flowchart3](./flowchart3.svg)


