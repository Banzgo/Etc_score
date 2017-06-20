import sys


## Hold the Ground, Breakthrough, Capture the Flags, Secure Target
scenarios = ["HtG", "BT", "CtF", "ST"]
## Armies in alphabetical order
armies = ["BH", "DL", "DE", "DH", "EoS", "HE", "ID", "KoE", "OK", "OG", "SA", "SE", "VS", "UD", "VC", "WDG"]
## Players in team
players = []
## Scores for each scenario, for each army, for each player
scenario_scores = []

##	Input format syntax:
##		All player names
##		{ for each scenario
##			Name of 1. scenario
##			8x Army + scenario_modifier for each player
##		}
##		Score
##		{ for each country
##			8x Country Army Player_score
##		}


def main():
	i_name = sys.argv[1]
	o_name = sys.argv[2]
	try:
		o_file = open(o_name, 'w')
		i_file = open(i_name, 'r')
	except FileNotFoundError:
		print('Wrong file names. Try again')
		return

	## Read players
	l = i_file.readline().strip()
	players = l.split( )
	scenario_scores = [[0 for j in range(len(armies))] for i in range(len(scenarios))]

	## Read scenarios 
	for i in range(len(scenarios)):
		## Read and discard headerline
		i_file.readline()
		## Read line and add it to scenario scores (Keeping army name)
		for a in range(len(armies)):
			l = i_file.readline().strip().split( )
			scenario_scores[i][a] = l

	## Read one header line.
	l = i_file.readline().strip()
	if l != "Score":
		print("Invalid syntax after scenarios.")
		return

	## Write header line
	o_file.write("PMP\t3\t" + str(len(scenarios)) + "\t" + "\t".join(scenarios)+ "\t" + "\t".join(players))
	
	## Read lines until out of countires
	while True:
		l = i_file.readline().strip().split( )
		if l == []:
			break
		else:
			country = l.pop(0)
			army = l.pop(0)
			new_line = country + "\t" + army + "\t"
			## For each player: Score, Score, 4x scenario modifier
			for p in range(len(players)):
				new_line += l[p] + "\t" + l[p] + "\t"
				index = armies.index(army)
				for s in range(len(scenarios)):
					new_line += scenario_scores[s][index][p+1] + "\t"
			## Write line
			o_file.write("\n" + new_line[:-1])
	## Close files
	o_file.close()
	i_file.close()

if __name__ == '__main__':
	if len(sys.argv) == 3:
		main()
	else:
		print('Wrong arguments -> python etc_score input.txt output.txt')