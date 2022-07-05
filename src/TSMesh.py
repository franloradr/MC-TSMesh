###########################################################################################
##### ROUTER ##############################################################################
###########################################################################################

class router(object):
    
    def __init__(self, posx, posy, radius=None):

        self.__radius = radius

        self.__posx = posx

        self.__posy = posy
        
    @property
    def radius(self):
        return self.__radius
        
    @property
    def posx(self):
        return self.__posx
        
    @property
    def posy(self):
        return self.__posy
    
    def setRadius(self, value):
        self.__radius = value    
    
    def setPosx(self, value):
        self.__posx = value
    
    def setPosy(self, value):
        self.__posy = value
        
    @property    
    def str(self):
        cad = "[X: "+str(self.posx)+", Y: "+str(self.posy)+", Radio: "+str(self.radius)+"]"
        return cad
               
    def __repr__(self):
        return self.str
	
###########################################################################################
##### CLIENT ##############################################################################
###########################################################################################	

class client(object):
    
    def __init__(self, posx, posy):
        
        self.__posx = posx

        self.__posy = posy

    @property
    def posx(self):
        return self.__posx
        
    @property
    def posy(self):
        return self.__posy
        
    @property    
    def str(self):
        cad = "[X: "+str(self.posx)+", Y: "+str(self.posy)+"]"
        return cad
               
    def __repr__(self):
        return self.str
		
#############################################################################################
##### MOVEMENT ##############################################################################
#############################################################################################

class movement(object):
    
    def __init__(self, type, router_to_moveToCell=None, posx_to_moveToCell=None, posy_to_moveToCell=None, router1_to_swap=None, router2_to_swap=None):

         self.__type = type

         self.__router_to_moveToCell = router_to_moveToCell

         self.__posx_to_moveToCell = posx_to_moveToCell

         self.__posy_to_moveToCell = posy_to_moveToCell

         self.__router1_to_swap = router1_to_swap

         self.__router2_to_swap = router2_to_swap
         
         self.__LastIterationAsTabu = 0 
                 
    @property
    def type(self):
        return self.__type
    
    @property
    def router_to_moveToCell(self):
        return self.__router_to_moveToCell
        
    @property
    def posx_to_moveToCell(self):
        return self.__posx_to_moveToCell
        
    @property
    def posy_to_moveToCell(self):
        return self.__posy_to_moveToCell
        
    @property
    def router1_to_swap(self):
        return self.__router1_to_swap
        
    @property
    def router2_to_swap(self):
        return self.__router2_to_swap
        
    @property
    def LastIterationAsTabu(self):
        return self.__LastIterationAsTabu
        
    def setLastIterationAsTabu(self, value):
        self.__LastIterationAsTabu = value
        
    @property    
    def str(self):
        
        cad = ""
        if(self.type == "swap"):
            cad += "[type: swap, "+str(self.router1_to_swap)+"<->"+str(self.router2_to_swap)+"]"
        else:
            if(self.type == "moveToCell"):
                cad += "[type: moveToCell, "+str(self.router_to_moveToCell)+"->("+str(self.posx_to_moveToCell)+", "+str(self.posy_to_moveToCell)+")]"                
        return cad
               
    def __repr__(self):
        return self.str

###########################################################################################
##### SOLUTION ############################################################################
###########################################################################################
		
class solution(object):
    
    def __init__(self, routers, precededSolution=None, appliedMovement=None):
        
        self.__routers = routers
        
        self.__fitnessValue = None
        
        self.__lengthGreatestConnectedSet = None
        
        self.__numberClientsCovered = None

        self.__precededSolution = precededSolution

        self.__appliedMovement = appliedMovement
    
    def modify(self, index, posx=None, posy=None, precededSolution=None, appliedMovement=None):
        
        if(not(isinstance(posx, type(None)))):
            self.__routers[index].setPosx(posx)
            
        if(not(isinstance(posy, type(None)))):
            self.__routers[index].setPosy(posy)  
        
        if(not(isinstance(precededSolution, type(None)))):
            self.__precededSolution = precededSolution
            
        if(not(isinstance(appliedMovement, type(None)))):
            self.__appliedMovement = appliedMovement
            
    @property
    def routers(self):
        return self.__routers
        
    @property
    def fitnessValue(self):
        return self.__fitnessValue
        
    def setFitnessValue(self,value):
        self.__fitnessValue = value
        
    @property    
    def numberClientsCovered(self):
        return self.__numberClientsCovered
        
    @property    
    def lengthGreatestConnectedSet(self):
        return self.__lengthGreatestConnectedSet
       
    def setNumberClientsCovered(self,value):
        self.__numberClientsCovered = value
    
    def setLengthGreatestConnectedSet(self,value):
        self.__lengthGreatestConnectedSet = value
    
    @property    
    def appliedMovement(self):
        return self.__appliedMovement
        
    @property    
    def precededSolution(self):
        return self.__precededSolution
    
    @property    
    def str(self):
        cad = "###########################################################################################"
        cad += "\n[\n"
        routers = self.routers
        for i in range(0, len(routers)):
            if(not(i+1==len(routers))):
                cad += "Router "+str(i)+": "+routers[i].str+",\n"
            else:
                cad += "Router "+str(i)+": "+routers[i].str
        cad += "\n]\n"
        cad += "lengthGreatestConnectedSet: "+str(self.lengthGreatestConnectedSet)+"\n"
        cad += "numberClientsCovered: "+str(self.numberClientsCovered)+"\n"
        
        if(not(isinstance(self.__appliedMovement, type(None)))):
            cad += "appliedMovement: "+self.__appliedMovement.str+"\n"
        cad += "###########################################################################################"
        return cad    
       
    def __repr__(self):
        return self.str
		
###########################################################################################
##### TSMESH ##############################################################################
###########################################################################################

class TSMeshAlgorithmProblem(object):
    
    def __init__(self, width, high, number_routers, number_clients, number_iterations, movement_type, 
                 tabu_size, elite_size, LARGE_HASH, max_number_iterations_without_improvement, 
                 probability_distribution, diversification_percentage, coverage_range):
        
        self.__width = width
        self.__high = high
        self.__number_routers = number_routers
        self.__number_clients = number_clients
        self.__number_iterations = number_iterations
        self.__movement_type = movement_type
        self.__tabu_size = tabu_size
        self.__elite_size = elite_size
        self.__LARGE_HASH = LARGE_HASH
        self.__coverage_range = coverage_range
        
###########################################################################################
####### DERIVATIVES #######################################################################
###########################################################################################
        
        self.__max_tabu_status = number_routers/2
        self.__aspiration_value = (self.__max_tabu_status/2) - log(self.__max_tabu_status, 2)
        
###########################################################################################
####### SOLUTIONS #########################################################################
###########################################################################################
        
        self.__current_solution = None
        self.__previous_current_solution = None
        self.__best_solution_found = None
        
###########################################################################################
####### CLIENTS ###########################################################################
###########################################################################################
        
        self.__clients = None
        
###########################################################################################
####### SHORT TERM MEMORY #################################################################
###########################################################################################
        
        self.__TL = None
        self.__hashing = None
        self.__TH = None
        
###########################################################################################
####### LONG TERM MEMORY ##################################################################
###########################################################################################
        
        self.__frecuency = None
        self.__most_frecuently_positions = None
        self.__tfrecuency = None
        self.__best_sols = None
        
###########################################################################################
####### ACTUAL ITERATION ##################################################################
###########################################################################################
        
        self.__actual_iteration = None
        
###########################################################################################
####### DIVERSIFICATION ###################################################################
###########################################################################################
        
        if(not(diversification_percentage >= 0.0 and diversification_percentage <= 1.0)):
            raise Exception("Error: el porcentaje de diversificación ha de estar comprendido entre 0.0 y 1.0")
        self.__diversification_percentage = diversification_percentage
        self.__number_iterations_without_improvement = None
        self.__max_number_iterations_without_improvement = max_number_iterations_without_improvement
        
###########################################################################################
####### DISTRIBUTION POINTS ###############################################################
###########################################################################################        

        self.__probability_distribution = probability_distribution

###########################################################################################
### MAIN METHOD ###########################################################################
###########################################################################################
    
    @property
    def executeTSMeshAlgorithm(self):
        self.__clients = self.compute_clients
        self.__current_solution = self.compute_initial_solution
        self.__best_solution_found = deepcopy(self.__current_solution)
        print(self.__current_solution)
        self.plot_solution(self.__current_solution)
        self.reset_TL
        self.reset_hashing
        self.reset_TH
        self.reset_frecuency
        self.reset_most_frecuently_positions
        self.reset_tfrecuency
        self.__best_sols = []
        self.__number_iterations_without_improvement = 0
        self.__actual_iteration = 0
        while(self.__actual_iteration < self.__number_iterations):
            Admissible = self.Admissible(self.__current_solution)
            self.__previous_current_solution = deepcopy(self.__current_solution)
            self.__current_solution = Admissible.pop(0)
            print(self.__current_solution)
            for solution in Admissible:
                print(solution)
                if(self.is_better_than(solution, self.__current_solution)):
                    self.__current_solution = solution
            if(self.is_better_than(self.__current_solution, self.__best_solution_found)):
                self.__best_solution_found = deepcopy(self.__current_solution)
                self.__number_iterations_without_improvement = 0
            else:
                self.__number_iterations_without_improvement += 1
            if((len(self.__best_sols) == self.__elite_size) and (self.__actual_iteration % self.__max_number_iterations_without_improvement) == 0):
                print "#Intensification"
                self.Intensification(self.__current_solution)
                print "#End_Intensification"
            if(self.__number_iterations_without_improvement == self.__max_number_iterations_without_improvement):
                print "#Diversification"
                self.Diversification(self.__current_solution)
                self.__number_iterations_without_improvement = 0
                print "#End_Diversification"
            self.update_recency(self.__current_solution)
            self.update_frecuency(self.__current_solution)
            self.__actual_iteration += 1
        print(self.__best_solution_found)
        self.plot_solution(self.__best_solution_found)
 
###########################################################################################
### PLOT ##################################################################################
###########################################################################################
        
    def plot_solution(self, solution):
        g = Graphics()
        for router in solution.routers:
            p = point((router.posx, router.posy), pointsize = 100)
            g += p.plot()
            c = circle((router.posx, router.posy), router.radius, rgbcolor = (1,0,0), linestyle = '--')
            g += c.plot()
        for client in self.__clients:
            p = point((client.posx, client.posy), pointsize = 50, rgbcolor = "green")
            g += p.plot()
        t = text(u""+solution.str+"\nlengthGreatestConnectedSet: "+str(solution.lengthGreatestConnectedSet)+"/"+str(self.__number_routers)+
                 "\nnumberClientsCovered: "+str(solution.numberClientsCovered)+"/"+str(self.__number_clients), 
                 (1,-4), 
                 bounding_box={'boxstyle':'round', 'fc':'w'}, horizontal_alignment="left"
                )
        g += t.plot()
        g.show(figsize=10)
        
###########################################################################################
### CLIENTS ###############################################################################
###########################################################################################
    
    @property
    def compute_clients(self):
        clients = self.random_2D_objects(self.__number_clients, self.__probability_distribution)
        return clients
    
    def random_2D_objects(self, number_points, probability_distribution, radius_range=None):
        res = []
        i=0
        while(i < number_points):
            if(probability_distribution == "Uniform"):
                a = 0
                b = self.__width-1
                c = self.__high-1
                T = RealDistribution('uniform', [a, b])
                posx = round(T.get_random_element())
                T = RealDistribution('uniform', [a, c])
                posy = round(T.get_random_element())
                if(not(isinstance(radius_range, type(None)))):
                    a = radius_range[1]
                    b = radius_range[0]
                    T = RealDistribution('uniform', [a, b])
                    radius = T.get_random_element()
                    res.append(router(posx, posy, radius))
                else:
                    res.append(client(posx, posy))
            else:
                if(probability_distribution == "Normal"):
                    print "WIP"
                else:
                    if(probability_distribution == "Exponential"):
                        print "WIP"
                    else:
                        if(probability_distribution == "Weibull"):
                            print "WIP"
            i += 1
        return res
        
###########################################################################################
### INITIAL SOLUTION ######################################################################
###########################################################################################
    
    @property
    def compute_initial_solution(self):
        routers = self.random_2D_objects(self.__number_routers, self.__probability_distribution, self.__coverage_range)
        initial_solution = solution(routers)
        self.compute_fitness_value(initial_solution)
        return initial_solution
    
    def compute_fitness_value(self, solution):
        length_greatest_connectedSet = self.compute_greatest_connectedSet(deepcopy(solution).routers)
        number_clients_covered = self.compute_number_clients_covered(solution.routers)
        solution.setLengthGreatestConnectedSet(length_greatest_connectedSet)
        solution.setNumberClientsCovered(number_clients_covered)
    
    def compute_greatest_connectedSet(self, nonConnectedSet):
        connectedSet = []
        new_nonConnectedSet = nonConnectedSet
        if(not(len(new_nonConnectedSet)==0)):
            connectedSet.append(new_nonConnectedSet.pop(0))
        if(nonConnectedSet==[]):
            return (len(connectedSet))
        else:
            i=0
            while(i<len(connectedSet)):
                j=0
                while(j<len(new_nonConnectedSet)):
                    distancia = sqrt((connectedSet[i].posx - new_nonConnectedSet[j].posx)^(2) + 
                                     (connectedSet[i].posy - new_nonConnectedSet[j].posy)^(2))
                    if(connectedSet[i].radius + new_nonConnectedSet[j].radius >= distancia):      
                        connectedSet.append(new_nonConnectedSet[j])
                        new_nonConnectedSet.pop(j) 
                        j=j-1
                    j=j+1    
                i=i+1
        return max(len(connectedSet), self.compute_greatest_connectedSet(new_nonConnectedSet))

    def compute_number_clients_covered(self, routers):
        res = 0
        for client in self.__clients:
            for router in routers:
                distancia = sqrt((router.posx-client.posx)^(2)+(router.posy-client.posy)^(2))
                if(distancia <= router.radius):
                    res = res + 1
                    break
        return res
    
###########################################################################################
### MEMORY ################################################################################
###########################################################################################
            
    @property
    def reset_TL(self):
        res = []
        for i in range(self.__number_routers):
            aux1 = []
            for j in range(self.__width):
                aux2 = []
                for k in range(self.__high):
                    aux2.append(-1)
                aux1.append(aux2)
            res.append(aux1)
        self.__TL = res
    
    @property
    def reset_hashing(self):
        res = []
        for i in range(self.__number_routers):
            aux1 = []
            for j in range(self.__width):
                aux2 = []
                for k in range(self.__high):
                    aux2.append(randint(1,self.__LARGE_HASH))
                aux1.append(aux2)
            res.append(aux1)
        self.__hashing = res 
    
    @property
    def reset_TH(self):
        res = [False]*self.__tabu_size
        self.__TH = res
        
    @property
    def reset_frecuency(self):
        res = []
        for i in range(self.__number_routers):
            aux1 = []
            for j in range(self.__width):
                aux2 = []
                for k in range(self.__high):
                    aux2.append(0)
                aux1.append(aux2)
            res.append(aux1)
        self.__frecuency = res
    
    @property
    def reset_most_frecuently_positions(self):
        res = []
        for j in range(self.__width):
            aux1 = []
            for k in range(self.__high):
                aux1.append(0)
            res.append(aux1)
        self.__most_frecuently_positions = res
    
    @property
    def reset_tfrecuency(self):
        res = [0]*self.__number_routers
        self.__tfrecuency = res
        
###########################################################################################
### ADMISSIBLE ############################################################################
###########################################################################################

    def Admissible(self, solution):
        Admissible = []
        Neighbourhood = []
        Tabu = []
        Aspiration = []
        for m in self.Movements(solution):
            newSolution = deepcopy(solution)
            self.apply_movement(newSolution, m)
            Neighbourhood.append(newSolution)
            if(not(self.__TH[self.hashing(newSolution) % self.__tabu_size] == True)):
                if(self.is_tabu(newSolution, m)):   
                    Tabu.append(newSolution)
                    if(self.aspirates(newSolution, m)):   
                        Aspiration.append(newSolution)
                        Tabu.remove(newSolution)
                else:
                    Admissible.append(newSolution)
            else:
                Tabu.append(newSolution)
        Admissible.extend(Aspiration)
        return Admissible
        
    def Movements(self, solution):
        Movements = []
        n = randint(0, 1)
        if(n==0):
            self.__movement_type = "swap"
        else:
            self.__movement_type = "moveToCell"
        if(self.__movement_type == "swap"):
            for i in range(0, len(solution.routers)):
                for j in range(i+1, len(solution.routers)):
                    Movements.append(movement("swap",None,None,None,i,j))
        else:
            if(self.__movement_type == "moveToCell"):
                i = randint(0, self.__number_routers-1)
                posx = randint(0, self.__width-1)
                posy = randint(0, self.__high-1)
                Movements.append(movement("moveToCell",i,posx,posy,None,None))
        return Movements
    
    def apply_movement(self, solution, movement):
        copy_solution = deepcopy(solution)
        if(movement.type == "swap"):
            solution.modify(movement.router1_to_swap, 
                            copy_solution.routers[movement.router2_to_swap].posx, 
                            copy_solution.routers[movement.router2_to_swap].posy
                           )
            solution.modify(movement.router2_to_swap, 
                            copy_solution.routers[movement.router1_to_swap].posx, 
                            copy_solution.routers[movement.router1_to_swap].posy,
                            copy_solution,
                            movement
                           )
        else:
            if(movement.type == "moveToCell"):
                solution.modify(movement.router_to_moveToCell, 
                                movement.posx_to_moveToCell, 
                                movement.posy_to_moveToCell,
                                copy_solution,
                                movement
                               )
        self.compute_fitness_value(solution)
        
    def hashing(self, solution):
        hash = 0
        for i in range(0, len(solution.routers)):
            hash += self.__hashing[i][solution.routers[i].posx][solution.routers[i].posy]
        return hash
        
    def is_tabu(self, solution, movement):
        res = False
        if(movement.type == "swap"):
            LastIterationAsTabu = [
                                   self.__TL[movement.router1_to_swap]
                                            [solution.routers[movement.router1_to_swap].posx]
                                            [solution.routers[movement.router1_to_swap].posy],
                                   self.__TL[movement.router2_to_swap]
                                            [solution.routers[movement.router2_to_swap].posx]
                                            [solution.routers[movement.router2_to_swap].posy]
                                  ]
            movement.setLastIterationAsTabu(LastIterationAsTabu)
            res = LastIterationAsTabu[0] > (-1) or LastIterationAsTabu[1] > (-1)
        else:
            if(movement.type == "moveToCell"):
                LastIterationAsTabu = (self.__TL[movement.router_to_moveToCell]
                                                [movement.posx_to_moveToCell]
                                                [movement.posy_to_moveToCell])
                movement.setLastIterationAsTabu(LastIterationAsTabu)
                res = LastIterationAsTabu > (-1)
        return res
        
    def aspirates(self, solution, movement):
        res = False
        if(self.is_better_than(solution, self.__best_solution_found)):
            res = True
        else:
            if(movement.type == "swap"):
                res = max(movement.LastIterationAsTabu[0],  movement.LastIterationAsTabu[1]) + self.__aspiration_value <= self.__actual_iteration
            else:
                if(movement.type == "moveToCell"): 
                    res = movement.LastIterationAsTabu + self.__aspiration_value <= self.__actual_iteration
        return res
        
    def is_better_than(self, solution1, solution2):
        res = False
        if(solution1.lengthGreatestConnectedSet > solution2.lengthGreatestConnectedSet):
            res = True
        else:
            if(solution1.lengthGreatestConnectedSet == solution2.lengthGreatestConnectedSet):
                if(solution1.numberClientsCovered > solution2.numberClientsCovered):
                    res = True
        return res
    
###########################################################################################
### RECENCY ###############################################################################
###########################################################################################
    
    def update_recency(self, solution):
        self.__TH[self.hashing(solution) % self.__tabu_size] == True
        if(self.hashing(self.__previous_current_solution) != self.hashing(solution)):
            if(movement.type == "swap"):
                print("hola")
                (self.__TL[solution.appliedMovement.router1_to_swap]
                          [solution.precededSolution.routers[solution.appliedMovement.router1_to_swap].posx]
                          [solution.precededSolution.routers[solution.appliedMovement.router1_to_swap].posy]) = self.__actual_iteration
                (self.__TL[solution.appliedMovement.router2_to_swap]
                          [solution.precededSolution.routers[solution.appliedMovement.router2_to_swap].posx]
                          [solution.precededSolution.routers[solution.appliedMovement.router2_to_swap].posy]) = self.__actual_iteration
            else:
                if(movement.type == "moveToCell"):
                    (self.__TL[solution.appliedMovement.router_to_moveToCell]
                              [solution.precededSolution.routers[solution.appliedMovement.router_to_moveToCell].posx]
                              [solution.precededSolution.routers[solution.appliedMovement.router_to_moveToCell].posy]) = self.__actual_iteration
        
###########################################################################################
### FRECUENCY #############################################################################
###########################################################################################
        
    def update_frecuency(self, solution):
        if(self.hashing(self.__previous_current_solution) != self.hashing(solution)):
            if(solution.appliedMovement.type == "swap"):
                
                self.__tfrecuency[solution.appliedMovement.router1_to_swap] += 1
                self.__tfrecuency[solution.appliedMovement.router2_to_swap] += 1
                
                (self.__frecuency[solution.appliedMovement.router1_to_swap]
                                 [solution.precededSolution.routers[solution.appliedMovement.router2_to_swap].posx]
                                 [solution.precededSolution.routers[solution.appliedMovement.router2_to_swap].posy]) += 1
                (self.__frecuency[solution.appliedMovement.router2_to_swap]
                                 [solution.precededSolution.routers[solution.appliedMovement.router1_to_swap].posx]
                                 [solution.precededSolution.routers[solution.appliedMovement.router1_to_swap].posy]) += 1
                                 
                (self.__most_frecuently_positions[solution.precededSolution.routers[solution.appliedMovement.router2_to_swap].posx]
                                                 [solution.precededSolution.routers[solution.appliedMovement.router2_to_swap].posy]) += 1
                (self.__most_frecuently_positions[solution.precededSolution.routers[solution.appliedMovement.router1_to_swap].posx]
                                                 [solution.precededSolution.routers[solution.appliedMovement.router1_to_swap].posy]) += 1
            else:
                if(solution.appliedMovement.type == "moveToCell"):
                    
                    self.__tfrecuency[solution.appliedMovement.router_to_moveToCell] += 1
                    
                    (self.__frecuency[solution.appliedMovement.router_to_moveToCell]
                                     [solution.appliedMovement.posx_to_moveToCell]
                                     [solution.appliedMovement.posy_to_moveToCell]) += 1
                                     
                    (self.__most_frecuently_positions[solution.appliedMovement.posx_to_moveToCell]
                                                     [solution.appliedMovement.posy_to_moveToCell]) += 1
                                                     
        if(len(self.__best_sols) < self.__elite_size):
            self.__best_sols.append(solution)
        else:
            min = self.__best_sols[0]
            for i in range(0, len(self.__best_sols)):
                if(not(self.is_better_than(self.__best_sols[i], min))):
                    min = self.__best_sols[i]
            if(self.is_better_than(solution, min)):
                self.__best_sols.remove(min)
                self.__best_sols.append(solution)

###########################################################################################
### INTENSIFICATION #######################################################################
###########################################################################################

    def Intensification(self, solution):
        i = 0
        while(i < self.__number_routers):
            sum = 0
            ri = []
            for j in range(0, len(self.__best_sols)):
                sum += self.__frecuency[i][self.__best_sols[j].routers[i].posx][self.__best_sols[j].routers[i].posy]
                ri.append([i,
                           j,
                           self.__best_sols[j].routers[i].posx, 
                           self.__best_sols[j].routers[i].posy,
                           self.__frecuency[i][self.__best_sols[j].routers[i].posx][self.__best_sols[j].routers[i].posy]
                          ]
                         )
            ri.sort(key=lambda x: x[4], reverse=True)
            if(not(len(ri)==0 or sum==0)):
                self.roulette_wheel_criteria(solution, ri, sum)
            i += 1

    def roulette_wheel_criteria(self, solution, ri, sum):
        random = uniform(0, 1)
        acumulative_sum = 0
        for i in range(0, len(ri)):
            acumulative_sum += ri[i][4]/sum
            if(acumulative_sum > random):
                move = movement("moveToCell", ri[i][0], ri[i][2], ri[i][3], None, None)
                break
        sys.setrecursionlimit(10000)
        self.apply_movement(solution, move)
        
###########################################################################################
### DIVERSIFICATION #######################################################################
###########################################################################################
    
    def Diversification(self, solution):
        sorted_tfrecuency = sorted([[i, self.__tfrecuency[i]] for i in range(0, len(self.__tfrecuency))], 
                                   key=lambda x: x[1]
                                  )
        most_frecuently_positions = []
        for i in range(0, len(self.__most_frecuently_positions)):
            for j in range(0, len(self.__most_frecuently_positions[i])):
                most_frecuently_positions.append([self.__most_frecuently_positions[i][j],i,j])
        sorted_most_frecuently_positions = sorted(most_frecuently_positions,
                                                  key=lambda x: x[0], 
                                                  reverse=True)
        for i in range(0, int(self.__diversification_percentage * self.__number_routers)):
            res = False
            j = 0
            for router in solution.routers:
                if(router.posx == sorted_most_frecuently_positions[i][1] 
                   and
                   router.posy == sorted_most_frecuently_positions[i][2]
                  ):
                       res = True
                       break
                else:
                    j += 1
            if(res == True):
                move = movement("swap",
                                None,
                                None,
                                None,
                                sorted_tfrecuency[i][0],
                                j
                               )
            else:
                move = movement("moveToCell",
                                sorted_tfrecuency[i][0],
                                sorted_most_frecuently_positions[i][1],
                                sorted_most_frecuently_positions[i][2],
                                None,
                                None
                               )
            self.apply_movement(solution, move)
            
###########################################################################################
### INSTANTIATION #########################################################################
###########################################################################################
		
def instantiateTSMeshAlgorithmProblem():
    instance = TSMeshAlgorithmProblem(16,16,4,12,64,"swap",51113,15,2^(32),10,"Uniform",0.25,[4, 1])
    instance.executeTSMeshAlgorithm
	
instantiateTSMeshAlgorithmProblem()