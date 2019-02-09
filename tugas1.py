def billing(ca,buss_hour,pickup,account_number):
    code=['sdfs','sdff','dsfe','dsff']
    dic_base={'base-fee1':50,'base-fee2':100,'base-fee3':500}
    dic_fee={'fee1':0,'fee_peripheral':10}
    
    if pickup=='yes':
        if buss_hour=='yes':
            if ca==1 or ca==2:
                base_fee=dic_base['base-fee1']/2
                additional_fee=dic_fee['fee1']
            elif (3<=ca<=10):
                base_fee=dic_base['base-fee2']/2
                additional_fee=dic_fee['fee_peripheral']*ca
            elif ca>10:
                base_fee=dic_base['base-fee3']/2
                additional_fee=dic_fee['fee_peripheral']*ca
        elif buss_hour=='no':
            if ca==1 or ca==2:
                base_fee=dic_base['base-fee1']*2/2
                additional_fee=dic_fee['fee1']
            elif (3<=ca<=10):
                base_fee=dic_base['base-fee2']*2/2
                additional_fee=dic_fee['fee_peripheral']*ca
            elif ca>10:
                base_fee=dic_base['base-fee3']*2/2
                additional_fee=dic_fee['fee_peripheral']*ca
    elif pickup=='no':
        if buss_hour=='yes':
            if ca==1 or ca==2:
                base_fee=dic_base['base-fee1']
                additional_fee=dic_fee['fee1']
            elif (3<=ca<=10):
                base_fee=dic_base['base-fee2']
                additional_fee=dic_fee['fee_peripheral']*ca
            elif ca>10:
                base_fee=dic_base['base-fee3']
                additional_fee=dic_fee['fee_peripheral']*ca
        elif buss_hour=='no':
            if ca==1 or ca==2:
                base_fee=dic_base['base-fee1']*2
                additional_fee=dic_fee['fee1']
            elif (3<=ca<=10):
                base_fee=dic_base['base-fee2']*2
                additional_fee=dic_fee['fee_peripheral']*ca
            elif ca>10:
                base_fee=dic_base['base-fee3']*2
                additional_fee=dic_fee['fee_peripheral']*ca
    if account_number in code:
        print('Account is VALID')
        total=base_fee+additional_fee
        print ('Base Fee = '+str(base_fee)+'\nAdditional Fee = '+str(additional_fee)) 
        print('Total = '+str(total))
    else:
        print('Account is NOT VALID')


     
