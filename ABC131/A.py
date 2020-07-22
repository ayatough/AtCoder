S = input()
black = ['11', '22', '33', '44', '55', '66', '77', '88', '99', '00'] 
print('Bad' if any(S.count(b) for b in black) else 'Good')
