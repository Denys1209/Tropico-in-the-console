from random import *
from time import *
start_time = time()
idiol = ["MIL", "KOM", "XRIST"]
name_idiol = ["миллитаристы","коммунисты","христиане"]
game = True
xod = 0
print("программа работает не выключается её")
class Fabric():
    name = ""
    how_mach = 0
    cost = 0
    opisanie = ""
    col_res = 0
    def __init__(self, cost, how_mach, name, col_res, proizwot_resurs):
        self.cost = cost
        self.how_mach = how_mach
        self.name = name
        self.col_res = col_res
        self.proizwot_resurs = proizwot_resurs
        self.opisanie = ("название = "+str(self.name)+" расходы = "+str(self.cost)+" стоимость = "+str(self.how_mach)+" количество производимого ресурса = "+str(self.col_res)+" производимый ресурс = "+str(self.proizwot_resurs.get_name()))
    def get_res(self):
        return self.col_res
    def gat_opis(self):
        print(self.opisanie)
    def get_cost(self):
        return self.cost
    def get_name(self):
        return self.name
    def get_how_mach(self):
        return self.how_mach
    def get_pro_res(self):
        return self.proizwot_resurs.get_name()



class Fabric_proizwot():
    name = ""
    how_mach = 0
    profit = 0
    opis = ""
    def __init__(self, name, how_mach, profit,how_much, resurs):
        self.name = name
        self.how_mach = how_mach
        self.profit = profit
        self.resurs = resurs
        self.how_much_res = how_much
        self.opis = ("название = "+self.name+" стоимость = "+str(self.how_mach)+" доходы = "+str(self.profit)+" количество потребяемого ресурса = "+str(self.how_much_res)+" потеряет ресурс = "+str(self.resurs.get_name()))
    def get_profit(self):
        return self.profit
    def get_how_much(self):
        return self.how_mach
    def get_profit(self):
        return self.profit
    def get_resurs(self):
        return self.resurs.get_name()
    def get_how_much_res(self):
        return self.how_much_res
    def gat_opis(self):
        return self.opis
    def get_name(self):
        return self.name
class bilding_par():
    
    name = ""
    how_mach = 0
    influzen_plus = 0
    influzen_minus = 0 
    cost = 0
    opisanie = ""
    def __init__(self, cost, name,  how_mach, influzen_plus, influzen_minus, par_plus, par_nimus ):
        self.cost = cost
        self.how_mach = how_mach
        self.name = name
        self.influzen_plus = influzen_plus
        self.influzen_minus = influzen_minus
        self.par_plus = par_plus
        self.par_minus = par_nimus
        self.opisanie = ("Стоимость = "+str(self.how_mach)+"$"
                         +", расходы = "+str(self.cost)+
                         ", название = "+str(self.name)+
                         ", негативное влияние на партию "+str(self.par_minus.get_norm_name())+
                         ", позитивное влияние на партию "+str(self.par_plus.get_norm_name())+
                         ", позитивное влияние в размере  = "+str(self.influzen_plus)+
                         ", негативное влияние в размере = "+str(self.influzen_minus)
                         )
    def get_cost(self):
        return self.cost
    def get_how_mach(self):
        return self.how_mach
    def gat_opis(self):
        print(self.opisanie)
    def oxtiveuchen_plus(self):
        return self.influzen_plus
    def oxtiveuchen_minus(self):
        return self.influzen_minus
    def get_name(self):
        return self.name
    def get_pard_plus(self):
        return self.par_plus.gat_name()
    def get_pard_minus(self):
        return self.par_minus.gat_name()
class bilding_from_populeter():
    plus_loil = 0
    how_much = 0
    name = ""
   
    cost = 0
    opis = ""
    def __init__(self, how_much, plus_loil, name, cost):
        self.how_much = how_much
        self.name = name
        self.plus_loil = plus_loil
        self.cost = cost
        self.opis = ("Стоимость = "+str(self.how_much)+"$"
                         +", расходы = "+str(self.cost)+
                         ", название = "+str(self.name)+
                         ", улучшает отношения народа на "+str(self.plus_loil)
                         )
    def get_cost(self):
        return self.cost
    def get_how_much(self):
        return self.how_much
    def get_name(self):
        return self.name
    def gat_opis(self):
        return self.opis
    def extive(self, pop):
        return pop.get_loiunosti() + self.plus_loil
class bilding_profid():
    name = ""
    profit = 0
    how_much = 0
    opis = ""
    def __init__(self, how_much, profit, name):
        self.how_much = how_much
        self.name = name
        self.profit = profit
        self.opis = ("Названия = "+str(self.name)+",  стоимость = "+str(self.how_much)+", доходы = "+str(self.profit))
    def get_how_much(self):
        return self.how_much
    def get_profit(self):
        return self.profit
    def get_name(self):
        return self.name
    def gat_opis(self):
        return self.opis



#all_fuctur = [bilding_par()]
class man():
    dahot_na_cusestuvani = 0
    nalog = 0
    bunt = 0
    #my_idiolog = ""
    my_zerp = 0
    clas = 0
    loi = 0
    def __init__(self, pa):
        self.my_idiolog = pa
        self.my_zerp = randint(1000, 6000)
        self.loi = randint(50, 100)
        self.set_clas()
    def get_idiol(self):
        return self.my_idiolog.gat_name()
    def get_nalog(self, nalog):
        if self.loi < 50:
            return int(self.my_zerp/100*(nalog-self.bunt))
        else:
            return int(self.my_zerp/100*nalog)
        
    def set_nalog(self, nal):
        self.nalog = nal
   
    def set_loil(self, loi):
        self.loi = loi
    def get_loiunosti(self):
        return self.loi
    def set_clas(self):
        if self.my_zerp >= 5000:
            self.clas = 1
            self.dahot_na_cusestuvani = 3500
        elif self.my_zerp >= 4000 and self.my_zerp <= 4999:
            self.clas = 2
            self.dahot_na_cusestuvani = 3000
        elif self.my_zerp >= 3000 and self.my_zerp <= 3999:
            self.clas = 3
            self.dahot_na_cusestuvani = 2500
        else:
            self.clas = 4
            self.dahot_na_cusestuvani = 2400
    def get_clas(self):
        return self.clas

    def loini(self):
        if self.dahot_na_cusestuvani<self.nalog:
            self.loi-=1+int(self.nalog/10)
            self.bunt += int(self.nalog/10)
        else:
            if self.bunt > 0:
                self.bunt -= 1
        if self.my_idiolog.get_loiunosti() > self.loi:
            self.loi-=1
        else:
            self.loi+=1
        self.loi-=3

   


class pati():
    who = []
    name = ""
    loiunosti = 0
    def __init__(self, name, norm_name):
        self.who = []
        self.name  = name
        self.norm_name = norm_name
        self.loiunosti = randint(50, 100)
    def push(self, manst):
        self.who.append(manst)
    def gat_name(self):
        return self.name
    def get_namber_who(self):
        return len(self.who)
    def get_loiunosti(self):
        return self.loiunosti
    def set_loiunosti(self, loi):
        self.loiunosti = loi
    def get_norm_name(self):
        return self.norm_name
class country():
    #class Budjet():
        #def __init__():
    priost_population = 2
    mans = 100
    next = 0
    population = []
    par = []
    many = 0
    PD_nalog = 20
    taxt_ma = []
    taxt_pa = []
    dob_profit = 0
    dob_rashot = 0
    how_mach_resurs = []
    fabricon = [[],[],[]]
    
           



            
    class resurs():
        name = ""
        profit_res = 0
        all_res = 0
        def __init__(self, name):
            self.name = name
      
        
        def get_name(self):
            return self.name
        
        def set_profit_res(self, r):
            self.profit_res += r
        def get_profit_res(self):
            return self.profit_res
        def get_all_res(self):
            return self.all_res
        def add_profit(self):
            self.all_res += self.profit_res
        def set_all_res(self, min_r):
            many = 0
            self.all_res -= min_r
            if self.all_res<0:
                for i in range(self.all_res, 0):
                    many -= 15000
                    self.all_res+=1
            return many

    class taxt_par():
        taxt = 0
        lgot = 0
        def __init__(self, taxt, par):
            self.par = par
            self.taxt = taxt
        def get_parti_name():
            return self.par.gat_name()
        def get_taxt(self):
            return self.taxt
        def set_taxt(self, ta):
            self.taxt = ta
        def set_lgot(self, ta):
            self.taxt = ta
        def get_lgot(self):
            return self.lgot
    class taxt_man():
        taxt = 0
        clas = 0
        lgot = 0
        def __init__(self, taxt, clas):
            self.clas = clas
            self.taxt = taxt

        def get_clas(self):
            return self.clas
        def set_taxt(self, ta):
            self.taxt = ta
        def set_lgot(self, ta):
            self.taxt = ta
        def get_lgot(self):
            return self.lgot
    def __init__(self):
        MIL = pati(idiol[0], name_idiol[0])
        KOM = pati(idiol[1], name_idiol[1])
        XRIST = pati(idiol[2], name_idiol[2])
        self.par.append(MIL)
        self.par.append(KOM)
        self.par.append(XRIST)
        self.set_population(self.next, self.mans)
        self.set_parti()
        self.set_PD()
        self.taxt_pa = [self.taxt_par(0, self.par[0]),self.taxt_par(0, self.par[1]),self.taxt_par(0, self.par[2])]
        self.taxt_ma =[self.taxt_man(0,1),self.taxt_man(0,2),self.taxt_man(0,3),self.taxt_man(0,4)]
        self.next = self.mans
        self.how_mach_resurs = [self.resurs("Нефть"), self.resurs("Золото"), self.resurs("Сталь"), 
                                self.resurs("Уран"), self.resurs("Хром"), self.resurs("Дерево"),
                                self.resurs("Пшено"), self.resurs("Доски"), self.resurs("Табак"),
                                self.resurs("Кукуруза"), self.resurs("Шкура"), self.resurs("Химические вещества")
                                ]
        self.fabric = [
            [bilding_profid(40000, 10000, "Банк"), ],
            [bilding_from_populeter(50000, 5, "Паб",5000 ),bilding_from_populeter(100000, 10, "Цирк", 10000 ), bilding_from_populeter(200000, 15, "Киностудия", 40000 ), bilding_from_populeter(200000, 15, "Театр", 50000 ), bilding_from_populeter(500000, 40, "Стадион", 100000 )], 
            [bilding_par(10000, "Полицейские участок", 50000, 10, 10, self.par[0], self.par[2]),bilding_par(15000, "Церковь", 60000, 10, 10, self.par[2], self.par[1]),bilding_par(15000, "Дом союза", 60000, 10, 10, self.par[1], self.par[0])],
            
            
            [Fabric(30000, 200000, "Нефтевышка", 5, self.how_mach_resurs[0]),Fabric(50000, 400000, "Золотая шахта", 4, self.how_mach_resurs[1]),Fabric(30000, 300000, "Сталелитейный завод", 8, self.how_mach_resurs[2]),
            Fabric(100000, 800000, "Урановая шахта", 10, self.how_mach_resurs[3]),Fabric(30000, 200000, "Металлургический завод", 5, self.how_mach_resurs[4]),Fabric(1000, 10000, "Леса пирка", 10, self.how_mach_resurs[5]),
            Fabric(10000, 100000, "Поля пшеницы", 6, self.how_mach_resurs[6]),Fabric(20000, 300000, "Деревообрабатывающий комбинат", 5, self.how_mach_resurs[7]),Fabric(10000, 200000, "Плантация табака", 5, self.how_mach_resurs[8]),
            Fabric(10000, 100000, "Поля кукурузы", 6, self.how_mach_resurs[9]),Fabric(20000, 300000, "Скота ферма", 10, self.how_mach_resurs[10]),Fabric(10000, 200000, "Хим лаборатория", 5, self.how_mach_resurs[11])
             ],
            [Fabric_proizwot("Завод для производства пластика", 500000, 100000, 10, self.how_mach_resurs[0]),Fabric_proizwot("Ювелирный завод", 700000, 100000, 8, self.how_mach_resurs[1]),Fabric_proizwot("4", 300000, 60000, 6, self.how_mach_resurs[2]),
            Fabric_proizwot("Ядерная электростанция", 7000000, 2000000, 40, self.how_mach_resurs[3]),Fabric_proizwot("Завод для производства нержавеющей стали", 600000, 200000, 10, self.how_mach_resurs[4]),Fabric_proizwot("Мебельный завод", 100000, 50000, 10, self.how_mach_resurs[5]),
            Fabric_proizwot("Хлеба булочный комбинат", 100000, 70000, 12, self.how_mach_resurs[6]),Fabric_proizwot("Верфь", 200000, 100000, 10, self.how_mach_resurs[7]),Fabric_proizwot("Сигарная фабрика", 500000, 300000, 10, self.how_mach_resurs[8]),
            Fabric_proizwot("Пищевая фабрика", 300000, 100000, 12, self.how_mach_resurs[9]),Fabric_proizwot("Швейная фабрика", 300000, 150000, 20, self.how_mach_resurs[10]),Fabric_proizwot("X", 600000, 300000, 10, self.how_mach_resurs[11]),
            ]]
    def set_population(self, namber, max_namber ):
        for i in range(namber, max_namber):
            m = man(self.par[randint(0, 2)])
            self.population.append(m)
        self.next = max_namber

    def set_parti(self, pop = 0):
        for a in range(pop, len(self.population)):
            if self.population[a].get_idiol() == "MIL":
                self.par[0].push(self.population[a])

            elif self.population[a].get_idiol() == "KOM":
                 self.par[1].push(self.population[a])
            elif self.population[a].get_idiol() == "XRIST":
                 self.par[2].push(self.population[a])

    def population_clas(self):
        one = 0
        two = 0
        thee = 0
        four = 0
        for i in range(0, len(self.population)):
            if self.population[i].get_clas() == 1:
                one +=1
            elif self.population[i].get_clas() == 2:
                two+=1
            elif self.population[i].get_clas() == 3:
                thee+=1
            elif self.population[i].get_clas() == 4:
                four+=1
        print("население = "+str(len(self.population)))
        print("1 класс = "+str(one))
        print("2 класс = "+str(two))
        print("3 класс = "+str(thee))
        print("4 класс = "+str(four))
    def set_PD(self):
        for i in range(0, len(self.population)):
            nal = 0
            self.many += self.population[i].get_nalog(self.PD_nalog)
            nal+=self.population[i].get_nalog(self.PD_nalog)
            for a in range(0, len(self.taxt_pa)):
                if self.population[i].get_idiol() == self.par[a].gat_name():
                    self.many += self.population[i].get_nalog(self.taxt_pa[a].get_taxt() - self.taxt_pa[a].get_lgot())
                    nal += self.population[i].get_nalog(self.taxt_pa[a].get_taxt() - self.taxt_pa[a].get_lgot())
                    break
            for y in range(0, len(self.taxt_ma)):
                if self.population[i].get_clas() == self.par[a].gat_name():
                    self.many += self.population[i].get_nalog(self.taxt_ma[a].get_taxt() - self.taxt_pa[a].get_lgot())
                    nal += self.population[i].get_nalog(self.taxt_ma[a].get_taxt() - self.taxt_pa[a].get_lgot())
                    break
            self.population[i].set_nalog(nal)
        self.many+=self.dob_profit-self.dob_rashot
        for i in range(0, len(self.how_mach_resurs)):
            self.how_mach_resurs[i].add_profit()
        for i in range(0, len(self.fabricon[2])):
            if self.fabricon[2][i].get_resurs() == self.how_mach_resurs[i].get_name():
                self.many += self.how_mach_resurs[i].set_all_res(self.fabricon[2][i].get_how_much_res())



    def get_many(self):
        return self.many

    def midl_loi(self):
        l = 0
        for i in range(0,  len(self.population)):
            l +=self.population[i].get_loiunosti()
        return l/int(len(self.population))

    def part(self):
        print("члены партий = "+str(self.par[0].get_namber_who())+" миллитаристы лояльность = "+str(self.par[0].get_loiunosti()))
        print("члены партий = "+str(self.par[1].get_namber_who())+" коммунисты лояльность = "+str(self.par[1].get_loiunosti()))
        print("члены партий = "+str(self.par[2].get_namber_who())+" христиане лояльность = "+str(self.par[2].get_loiunosti()))
    def funstor_all(self):
        #len(self.fabric)
        #print(str(i+1)+") "+self.fabric[i].get_name())
        print('''
        1)Здания которые приносят доход
        2)Здания для повышения лояльности населения
        3)Здания для повышения лояльности партий
        4)Здания производящие ресурсы
        5)Здания которые требують ресурсы
        ''')
        otvet = input("Укажите номер отдела чтобы вывести все здания: назад - exit")
        if otvet == "exit":
            return True
        otvet = int(otvet)-1
        for i in range(0, len(self.fabric[otvet])):
            print(str(i+1)+") "+self.fabric[otvet][i].get_name())
        otvet2 = input("Укажите номер здания чтобы вывести описания этого здания: назад - exit")
        if otvet == "exit":
            return True
        otvet2 = int(otvet2)-1
        if otvet == 2:
            self.fabric[otvet][otvet2].gat_opis()
        else:
            print(self.fabric[otvet][otvet2].gat_opis())
        pocup = input("строим? 1)ДА 2)НЕТ")
        #get_pard_plus
        if pocup == "1":
            if otvet  == 0:
                self.many -= self.fabric[otvet][otvet2].get_how_much()
                self.dob_profit += self.fabric[otvet][otvet2].get_profit()
                self.fabric[otvet][otvet2]
                self.fabricon[0].append(self.fabric[otvet][otvet2])
            elif otvet == 1:
                self.many -= self.fabric[otvet][otvet2].get_how_much()
                self.dob_rashot += self.fabric[otvet][otvet2].get_cost()
                for i in range(0, len(self.population)):
                    self.population[i].set_loil(self.fabric[otvet][otvet2].extive(self.population[i]))
            elif otvet == 2:
                for i in range(0, len(self.par)):
                    if self.fabric[otvet][otvet2].get_pard_plus() == self.par[i].gat_name():
                        self.par[i].set_loiunosti(self.par[i].get_loiunosti()+self.fabric[otvet][otvet2].oxtiveuchen_plus())
                        break
                for i in range(0, len(self.par)):
                    if self.fabric[otvet][otvet2].get_pard_minus() == self.par[i].gat_name():
                        self.par[i].set_loiunosti(self.par[i].get_loiunosti()-self.fabric[otvet][otvet2].oxtiveuchen_minus())
                        break
                self.dob_rashot+=self.fabric[otvet][otvet2].get_cost()
                self.many-=self.fabric[otvet][otvet2].get_how_mach()
            elif otvet == 3:
                self.dob_rashot += self.fabric[otvet][otvet2].get_cost()
                self.many -= self.fabric[otvet][otvet2].get_how_mach()
                for i in range(0, len(self.how_mach_resurs)):
                    if self.how_mach_resurs[i].get_name() == self.fabric[otvet][otvet2].get_pro_res():
                        self.how_mach_resurs[i].set_profit_res(self.fabric[otvet][otvet2].get_res())
                self.fabricon[1].append(self.fabric[otvet][otvet2])
                
            elif otvet == 4:
                self.dob_profit += self.fabric[otvet][otvet2].get_profit()
                
                self.many -= self.fabric[otvet][otvet2].get_how_much()
                self.fabricon[2].append(self.fabric[otvet][otvet2])



                


    def nalogi(self):
        print('''
        1)ПД - подоходный налог
        2)Льготы
        3)Дополнительные сборы и платежи
        ''')
        otvet = input()
        if otvet == "1":
            print("Подоходный налог = "+str(self.PD_nalog))
            print('''
            1)изменить ПД
            2)не изменять ПД
            ''')
            otvet = input()
            if otvet == "1":
                self.PD_nalog = int(input("Какой ПД"))
                print("ПД изменен")
        elif otvet == "2":
            print('''
            1)льготы на класс человека
            2)льготы на партию
            ''')
            otvet = input()
            if otvet == "1":
                print('''
                1)для 1 класс
                2)для 2 класс
                3)для 3 класс
                4)для 4 класс
                ''')
                otvet = input()
                if otvet == "1":
                    otvet = input("Какие льготы")
                    self.taxt_ma[0].set_lgot(int(otvet))
                elif otvet == "2":
                    otvet = input("Какие льготы")
                    self.taxt_ma[1].set_lgot(int(otvet))
                elif otvet == "3":
                    otvet = input("Какие льготы")
                    self.taxt_ma[2].set_lgot(int(otvet))
                elif otvet == "4":
                    otvet = input("Какие льготы")
                    self.taxt_ma[3].set_lgot(int(otvet))
            if otvet == "2":
                print('''
                1)для партий миллитаристов
                2)для партий христиан
                3)для партий коммунистов
                ''')
                otvet = input()
                if otvet == "1":
                    otvet = input("Какие льготы")
                    self.taxt_pa[0].set_lgot(int(otvet))
                elif otvet == "2":
                    otvet = input("Какие льготы")
                    self.taxt_pa[1].set_lgot(int(otvet))
                elif otvet == "2":
                    otvet = input("Какие льготы")
                    self.taxt_pa[2].set_lgot(int(otvet))
        elif otvet == "3":
            print('''
            1)доп сборы на класс человека
            2)сборы на партию
            ''')
            otvet = input()

            if otvet == "1":
                print('''
                1)для 1 класс
                2)для 2 класс
                3)для 3 класс
                4)для 4 класс
                ''')
                otvet = input()
                if otvet == "1":
                    otvet = input("Какой доп сбор")
                    self.taxt_ma[0].set_taxt(int(otvet))
                elif otvet == "2":
                    otvet = input("Какой доп сбор")
                    self.taxt_ma[1].set_taxt(int(otvet))
                elif otvet == "3":
                    otvet = input("Какой доп сбор")
                    self.taxt_ma[2].set_taxt(int(otvet))
                elif otvet == "4":
                    otvet = input("Какой доп сбор")
                    self.taxt_ma[3].set_taxt(int(otvet))
            if otvet == "2":
                print('''
                1)для партий миллитаристов
                2)для партий христиан
                3)для партий коммунистов
                ''')
                otvet = input()
                if otvet == "1":
                    otvet = input("Какой доп сбор")
                    self.taxt_pa[0].set_taxt(int(otvet))
                elif otvet == "2":
                    otvet = input("Какой доп сбор")
                    self.taxt_pa[1].set_taxt(int(otvet))
                elif otvet == "2":
                    otvet = input("Какой доп сбор")
                    self.taxt_pa[2].set_taxt(int(otvet))
    def resur_on_sc(self):
        for i in range(0, len(self.how_mach_resurs)):
            print(str(i+1)+")"+self.how_mach_resurs[i].get_name()+" производства = "+str(self.how_mach_resurs[i].get_profit_res())+" на складе = "+str(self.how_mach_resurs[i].get_all_res()))
    def set_loian(self):
        for i in range(0, len(self.population)):
            self.population[i].loini()
            if self.population[i].get_loiunosti() > 100:
                self.population[i].set_loil(100)
        for i in range(0, len(self.par)):
            self.par[i].loiunosti = self.par[i].get_loiunosti() - 1

    def set_pop_plus(self):
        self.mans += self.mans/100*self.priost_population

        self.set_population(self.next, int(self.mans))
    def event_bilding(self):
        
        chast_2 = [" случился потоп.", " произошел пожар.", " произошло землетрясение."," случилось наводнение."]
        opis = "В "
          
        
        g =False
        for i in range(0, len(self.fabricon)):
            if len(self.fabricon[i]) != 0:
                ran = randint(0, len(self.fabricon[i])-1)
                g =True
                if g:
                    if i == 0:
                        r = randint(0, len(chast_2)-1)
                        opis +=self.fabricon[0][ran].get_name()+chast_2[r]
                        print(opis)
                        self.dob_profit -=self.fabricon[0][ran].get_profit()
                        self.fabricon[0].pop(ran)
                        break
                    elif i == 1:

                        for i in range(0, len(self.how_mach_resurs)):
                            if self.how_mach_resurs[i].get_name() == self.fabricon[1][ran].get_pro_res():
                                r = randint(0, len(chast_2)-1)
                                opis +=self.fabricon[1][ran].get_name()+chast_2[r]
                                print(opis)
                                self.how_mach_resurs[1].set_profit_res(-self.fabricon[1][ran].get_res())
                                self.dob_rashot -= self.fabricon[1][ran].get_cost
                                self.fabricon[1].pop(ran)
                                break
                                
                    elif i ==2:
                        for a in range(0, len(self.how_mach_resurs)):
                            if self.how_mach_resurs[a].get_name() == self.fabricon[2][ran].get_resurs():
                                r = randint(0, len(chast_2)-1)
                                self.dob_profit -= self.fabricon[2][ran].get_profit()
                                opis +=self.fabricon[2][ran].get_name()+chast_2[r]
                                self.fabricon[2].pop(ran)
                                print(opis)
                                break
                                
                    break
    def event_infest(self):

        chact1 = "Эпидемия "
        chact2 = ["кори", "чумы", "коронавируса"]
        chact3 = [" на севере"," в городе мон", " в городе порте ", " в регионе норт"]
        min_man = int(len(self.population)/10)
        r = randint(0, len(chact2)-1)
        r2 = randint(0, len(chact3)-1)
        opis = ""
        mi_many = 5000*min_man
        self.many -= mi_many
        opis += chact1+chact2[r]+chact3[r2]+" смерти = "+str(min_man)+" затраты = "+str(mi_many)+"$"
        print(opis)
        for i in range(0, min_man):
            self.population.pop(i)
    def partion_negativ(self):
        r = randint(0, len(name_idiol)-1)
        nim_loi = randint(5, 20)
        opis = name_idiol[r]+" снижение лояльности на "+str(nim_loi)
        self.par[r].set_loiunosti(self.par[r].get_loiunosti() - nim_loi)
        print(opis)
    def profit_add_event(self):
        prof_dob = randint(1000, 10000)
        chast = ["Мы нашли золото ", "Мы обнаружили нефть ", "У нас открылось отделение CEE"]
        r = randint(0, len(chast)-1)
        opis = chast[r]+"прибыль увеличивается за ход на "+str(prof_dob)+"$"
        self.dob_profit += prof_dob
        print(opis)
    def one_add_many(self):
        chast1 = ["Нам направила помощь США ", "Помощь от ООН ", "Помощь от Израиля "]
        many = randint(10000, 100000)
        r = randint(0, len(chast1)-1)
        opis = chast1[r]+" в размере "+str(many)+"$"
        self.many += many
        print(opis)
 
    #def add_bulding_event(self):
        
                                
                    

my_count = country()
my_count.set_PD()







def menu():
    game_local = True
    
    while game_local:
        print(str(my_count.get_many())+"$")
        print('''
    1)партии
    2)налоги
    3)население
    4)строительство
    5)следующий ход
    6)ресурсы на складе
    exit = Выход из игры
        ''')
        otvet = input()
        if otvet == "1":
            my_count.part()
        elif otvet == "2":
            my_count.nalogi()
        elif otvet == "3":
            print("Средняя лояльность = "+str(int(my_count.midl_loi())))
            my_count.population_clas()
        elif otvet == "4":
            my_count.funstor_all()
        elif otvet == "5":
            game_local = False
        elif otvet == "6":
            my_count.resur_on_sc()
        elif otvet == "exit":
            return False
            #game_local = False
    return True

while menu():
    my_count.set_pop_plus()
    my_count.set_PD()
    my_count.set_loian()
    xod +=1
    print("Ход "+str(xod))
    if my_count.many < -1000:
        print("Ваша страна банкрот")
        break
    if my_count.midl_loi()<0:
        print("Произошла революция")
        break
        
    if xod%6 == 0:
        eve = randint(0, 2)
        if eve == 0:
            my_count.event_infest()
        elif eve == 1:
            my_count.event_bilding()
        elif eve == 2:
            my_count.partion_negativ()
    if xod%4 == 0:
        eve = randint(0, 1)
        if eve == 0:
            my_count.one_add_many()
        elif eve == 1:
            my_count.profit_add_event()

        
   
       
print("Конец")
        
