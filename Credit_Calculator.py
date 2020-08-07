import sys
import math
import argparse

error = "Incorrect parameters."


def main():
    parser = argparse.ArgumentParser(description='Credit Calculator')
    parser.add_argument("--type", help="Desired Calculation", type=str)
    parser.add_argument("--principal", help="Initial credit principal", type=float)
    parser.add_argument("--periods", help="Number of months", type=int)
    parser.add_argument("--interest", help="Yearly interest rate", type=float)
    parser.add_argument("--payment", help="Monthly payment", type=float)
    args = parser.parse_args()
    sys.stdout.write(str(credit_calc(args)))


def credit_calc(args):

    if not args.interest:
        print(error)
    else:
        if (args.payment or args.principal or args.periods or args.interest) <= 0:  # NEGATIVE VALUES ENTERED CHECKER
            print(error)

        if args.type == 'annuity':

            if not args.principal and not args.periods:
                print(error)

            if not args.payment:
                # use periods, principal, and interest

                nominal_interest_rate = (args.interest / 100) / 12

                numerator = nominal_interest_rate * (1 + nominal_interest_rate) ** args.periods
                denominator = ((1 + nominal_interest_rate) ** args.periods) - 1

                annuity_payment = args.principal * (numerator / denominator)

                overpayment = math.ceil(annuity_payment) * args.periods - args.principal

                print('Your annuity payment = ' + str(int(math.ceil(annuity_payment))) + '!\n\nOverpayment = ' + str(
                    int(math.ceil(overpayment))))

            if not args.periods:
                # use interest, payment, and principal

                nominal_interest_rate = (args.interest / 100) / 12

                denominator = args.payment - nominal_interest_rate * args.principal  # CODE SHORTENING VARIABLE
                count_of_periods = math.ceil(math.log(args.payment / int(denominator), 1 + nominal_interest_rate))

                if count_of_periods == 1:
                    overpayment = math.ceil(args.payment) * count_of_periods - args.principal
                    print('It takes 1 month to repay the credit!\n\nOverpayment = ' + str(
                        math.ceil(overpayment)))  # OFF-CASE OUTPUT FOR SINGULAR "MONTH"

                elif 1 != count_of_periods < 12:
                    overpayment = math.ceil(args.payment) * count_of_periods - args.principal
                    print('It takes ' + str(count_of_periods) + ' months to repay the credit!\n\nOverpayment = ' + str(
                        math.ceil(overpayment)))
                else:
                    count_of_years = int(math.floor(count_of_periods / 12))
                    months_remaining = int(math.ceil(count_of_periods % 12))
                    if count_of_years == 1 and months_remaining > 0:
                        overpayment = math.ceil(args.payment) * count_of_periods - args.principal
                        print('It takes 1 year and ' + str(months_remaining) + ' to repay the credit!\n\nOverpayment = '
                              + str(int(math.ceil(overpayment))))
                    elif months_remaining == 0:
                        overpayment = math.ceil(args.payment) * count_of_periods - args.principal
                        print('It takes ' + str(count_of_years) + ' years to repay the credit!\n\nOverpayment = ' + str(
                            int(math.ceil(overpayment))))
                    else:
                        # MIGHT MESS EVERYTHING UP
                        overpayment = math.ceil(args.payment) * count_of_periods - args.principal
                        print('It takes ' + str(count_of_years) + ' years and '
                              + str(months_remaining) + ' months to repay the credit!\n\nOverpayment = '
                              + str(math.ceil(overpayment)))

            if not args.principal:
                nominal_interest_rate = (args.interest / 100) / 12
                denom_numerator = nominal_interest_rate * math.pow(1 + nominal_interest_rate, args.periods)
                denom_denominator = math.pow(1 + nominal_interest_rate, args.periods) - 1
                credit_principal = args.payment / (denom_numerator / denom_denominator)

                overpayment = math.ceil(args.payment) * args.periods - credit_principal

                print('Your credit principal = ' + str(int(credit_principal)) + '!\n\nOverpayment = ' + str(
                    int(math.ceil(overpayment))))

        elif args.type == 'diff':

            if args.principal and args.periods and args.interest:

                m = 0
                total = 0
                nominal_interest_rate = (args.interest / 100) / 12

                for month in range(int(args.periods)):
                    m += 1
                    part_2 = args.principal - ((args.principal * (m - 1)) / args.periods)
                    differentiated_payment = math.ceil(args.principal / args.periods + nominal_interest_rate * part_2)
                    total += differentiated_payment
                    print("Month " + str(m) + ": paid out " + str(int(differentiated_payment)))
                    # print(f"Month {m}: paid out 'ROUNDED' {round(differentiated_payment)}")
                overpayment = total - args.principal
                print('\nOverpayment = ' + str(int(overpayment)))

            else:
                print(error)
        else:
            print(error)


if __name__ == '__main__':
    main()
