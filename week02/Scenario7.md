Q.A program is required to read customer's name, a purchase amount and a tax code. The tax code has been validaded and will one of the following.

1. tax tempt(0%)
1. state sales tax only(3%)
1. federal and state sales tax(5%)
1. special sales tax(5%)

IF statement
```psuedocode
BEGIN
  READ name, purch_amt, tax_code

  IF tax_code = 0 THEN
      sales_tax = 0
  ELSE
      IF tax_code = 1 THEN
          sales_tax = purch_amt * 0.03
      ELSE
          IF tax_code = 2 THEN
              sales_tax = purch_amt * 0.05
          ELSE
              IF tax_code = 3 THEN
                  sales_tax = purch_amt * 0.07
              ENDIF
          ENDIF
      ENDIF
  ENDIF

  total_amt = purch_amt + sales_tax
  DISPLAY name, purch_amt, sales_tax, total_amt
END
```
IN CASE statement
```psuedocode
BEGIN
    READ name, purch_amt, tax_code
    CASE OF tax_code
        0：sales_tax = 0
        1：sales_tax = purch_amt * 0.03
        2：sales_tax = purch_amt * 0.05
        0：sales_tax = purch_amt * 0.07
    total_amt = purch_amt + sales_tax
    DISPLAY name, purch_amt, sales_tax, total_amt
END
```