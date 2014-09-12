#hw1p3

class RockPaperScissors 	
	class NoSuchStrategyError < StandardError
	end
	
	def self.winner(p1, p2)
		#print p1, p2
		#can refactor with more descriptive names, variables below
		#@p1name = p1[0]
		#@p2name = p2[0]
		@p1strategy = p1[-1]
		@p2strategy = p2[-1]
		strats = ["R", "P", "S"]
		raise NoSuchStrategyError.new, "Strategy must be one of R,P,S" unless (strats.include?(@p1strategy) && strats.include?(@p2strategy))
		return p1 if p1[-1] == p2[-1]
		if p1[-1] == "P"
			return p1 if p2[-1] == "R"
			return p2
		elsif p1[-1] == "S"
			return p1 if p2[-1] == "P"
			return p2
		elsif p1[-1] == "R"
			return p1 if p2[-1] == "S"
			return p2
		end
	end

	def self.tournament_winner(p1)
		print "entered"
		while p1[0][0][0].is_a? Array #checks if any arrays left otherwise uses last 2 array items
			# print p1[0][0][0]
			# print "\n"
			p1[0][0] = winner(p1[0][0][0], p1[0][0][1])
			p1[0][1] = winner(p1[0][1][0], p1[0][1][1])
		end
		print "second"
		while p1[1][0][0].is_a? Array #checks if any arrays left
			#print p1[1][0][0]
			#print p1[1][1][0]
			p1[1][0] = winner(p1[1][0][0], p1[1][0][1])
			p1[1][1] = winner(p1[1][1][0], p1[1][1][1])
		end
		if p1[0][1].is_a? Array
			p1[0] = winner(p1[0][0], p1[0][1])
			p1[1] = winner(p1[1][0], p1[1][1])
		end
		winner(p1[0], p1[1])
	end
end
#print "\n"
#print "\n"

# a = RockPaperScissors.new
# rock = ['Armando','R'] ; paper = ['Dave','P']
# #print "\n"
# print RockPaperScissors.tournament_winner([rock,paper]) == paper
#print "\n"
# print a.tournament_winner([
#     [
#         [ ["Armando", "P"], ["Dave", "S"] ],
#         [ ["Richard", "R"],  ["Michael", "S"] ],
#     ],
#     [
#         [ ["Allen", "S"], ["Omer", "P"] ],
#         [ ["David E.", "R"], ["Richard X.", "P"] ]
#     ]
# ])
# print "\n"
# scissors = ['Sam','S']
# print RockPaperScissors.winner(rock, scissors) == rock
# tourney = [

# [
#   [ ["Armando", "P"], ["Dave", "S"] ],      
#   [ ["Richard", "R"], ["Michael", "S"] ]
# ],
# [
#   [ ["Allen", "S"], ["Omer", "P"] ],
#   [ ["David E.", "R"], ["Richard X.", "P"] ]
# ]
# ]

#print RockPaperScissors.tournament_winner(tourney)