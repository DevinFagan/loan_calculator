import math
import argparse

parser = argparse.ArgumentParser(description="This program calculates \
your loan payment.")
parser.add_argument('--type', type=str)
parser.add_argument('--payment', type=float)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=float)
parser.add_argument('--interest', type=float)
args = parser.parse_args()
try:
    num = 0
    m = 1
    if args.type == 'diff' and args.periods > 0 and args.principal > 0 and args.interest > 0:
        while m <= args.periods:
            print(f"Month {m}: payment is " + str(
                math.ceil((args.principal / args.periods) + (args.interest / (12 * 100)) * (args.principal -
                                                                                            (args.principal * (
                                                                                                        m - 1) / args.periods)))))
            num += math.ceil(
                (args.principal / args.periods) + (args.interest / (12 * 100)) * (
                            args.principal - (args.principal * (m - 1)
                                              / args.periods)))
            m += 1

        print(f"\nOverpayment = {round(num - args.principal)}")

    elif args.type == 'annuity' and args.payment is None and args.periods > 0 and args.principal > 0 and args.interest > 0:

        args.payment = math.ceil(
            args.principal * (((args.interest / (12 * 100)) * ((1 + (args.interest / (12 * 100))) ** args.periods)) /
                              (((1 + (args.interest / (12 * 100))) ** args.periods) - 1)))

        print(f"Your monthly payment = {args.payment}!")
        print(f"Overpayment = {round((args.payment * args.periods) - args.principal)}")

    elif args.type == 'annuity' and args.principal is None and args.payment > 0 and args.periods > 0 and args.interest > 0:

        args.principal = math.ceil(
            (args.payment / (((args.interest / (12 * 100)) * ((1 + (args.interest / (12 * 100))) ** args.periods)) /
                             (((1 + (args.interest / (12 * 100))) ** args.periods) - 1))))
        print(f"Your loan principal = {args.principal}!")
        print(f"Overpayment = {round((args.payment * args.periods) - args.principal)}")

    elif args.type == 'annuity' and args.periods is None and args.payment > 0 and args.principal > 0 and args.interest > 0:

        x = args.payment / (args.payment - (args.interest / (12 * 100)) * args.principal)
        args.periods = math.ceil(math.log(x, 1 + (args.interest / (12 * 100))))
        years, months = divmod(args.periods, 12)

        if years > 1 and months > 1:
            print(f"It will take {years} years and {months} months to repay this loan!")
        elif years == 1 and months == 1:
            print(f"It will take {years} year and {months} month to repay this loan!")
        elif years == 1 and months > 1:
            print(f"It will take {years} year and {months} months to repay this loan!")
        elif years > 1 and months == 1:
            print(f"It will take {years} years and {months} month to repay this loan!")
        elif years > 1 and months == 0:
            print(f"It will take {years} years to repay this loan!")
        elif years == 1 and months == 0:
            print(f"It will take {years} year to repay this loan!")
        elif years == 0 and months > 1:
            print(f"It will take {months} months to repay this loan!")
        else:
            print(f"It will take {months} month to repay this loan!")

        print(f"Overpayment = {round((args.payment * args.periods) - args.principal)}")

    else:
        print("Incorrect parameters.")

except TypeError:
    print("Incorrect parameters.")

