while true:
    height = float(input('enter your height (cm):'))
    weight = float(input('enter your weight (kg):'))

    bmi =(weight/(height **2))

    if(16<bmi<18.5):
        print ( 'your bmi is: ',bmi,'your need to gain your weight:')

        break

    elif (18.5 <= bmi <24 ):
        print ( 'your bmi is: ',bmi,'your weight is normal:')

    elif (24 <= bmi < 30 ):
        print ( 'your bmi is: ',bmi,'your close  to overweight :')

    elif (30 <= bmi <35 ):
            print ('your bmi is: ',bmi,'you are a little overweigh :')

    elif (35 <= bmi < 40 ):
        print ('your bmi is: ',bmi,'you are a overweight:')

        break

    elif bmi >= 40:
        print('your bmi is: ',bmi,'you weight is too much!:')

        break

    else:
        print( 'information is incorrect!\ pleas try agine. :')
        continue 
