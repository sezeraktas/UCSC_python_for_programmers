 more = "birthday cake"
 more[-4:], more[9:], more[9:13]
(’cake’, ’cake’, ’cake’)
 more.split()[-1], more.split()[1]
(’cake’, ’cake’)
 more.rsplit(None, 1)[1], more.rsplit(None, 1)[-1]
(’cake’, ’cake’)


 metals = "silver gold copper platinum"
 " and ".join(metals.capitalize().split()) + " are only worth money."
’Silver and gold and copper and platinum are only worth money.’