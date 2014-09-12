class String
	def palindrome?
		self.reverse == self
	end
end

def count_words(str_in)
	str_hash = {}
	str_list = str_in.split
	str_list.each{ |x| str_hash[x] = str_list.count(x)}
	str_hash
end


#raise "Should be true" if "redivider".palindrome? != true
#raise "Should be False" if "adam".palindrome? != false

#print count_words("one two two")["two"] == 2



class Dessert
	def initialize(name, calories)
		@name = name
		@calories = calories
	end

	attr_accessor :name
	attr_accessor :calories

	def healthy?
		@calories <= 200
	end

	def delicious?
		true
	end
end

class JellyBean < Dessert
	def initialize(flavor)
		@calories = 5
		@flavor = flavor
		name = @flavor + " jelly bean"
		super(name,@calories)
	end

	attr_accessor :flavor

	def delicious?
		return false if @flavor == "licorice"
	end
end

a = Dessert.new("cake", 200)
#print a.delicious?
# print a.healthy?
# print "\n"
# print a.calories

# print "\n"
b = JellyBean.new("licorice")
print b.delicious?
print "\n"
c = JellyBean.new("strawberry")
print c.healthy?
print c.delicious?
print "\n"
print c.delicious?