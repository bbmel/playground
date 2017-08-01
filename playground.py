def cigar_party(cigars, is_weekend):
    if cigars >= 40 and is_weekend:
        print('True')
    elif cigars >= 40 and cigars <= 60:
        print('True')
    else:
        print('False')


cigar_party(30, False)
cigar_party(50, False)
cigar_party(70, True)
