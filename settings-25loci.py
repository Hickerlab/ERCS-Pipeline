sampleA = [(250, 750), (240, 740), (240, 760), (260, 740), (260, 760)]
sampleB = [(750, 750), (740, 740), (740, 760), (760, 740), (760, 740)]
sampleC = [(250, 250), (240, 240), (240, 260), (260, 240), (260, 260)]
sampleD = [(750, 250), (740, 240), (740, 260), (760, 240), (760, 260)]
sample = sampleA + sampleB + sampleC + sampleD

settings = {
	### ERCS Settings ###
	'landscape_size': 1000,
	# Need to update GeneSamples_TEMPLATE.arp if you change this.
	'sample_locations': sample,

	# The number of recombination proobabilities determines the number of loci.
	'recombination_probabilities': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
	'num_replicates': 10000,
	
	# rate in events per 1000/gen
	'small_event': {'rate': (1000.0, 1000.0), 'radius': (20, 20), 'u': 1.0},
	'large_event': {'rate': (1.0, 100.0), 'radius': (50, 300), 'u': 0.25},
	
	### SeqGen Settings ###
	'mutation_rate': 1.1e-8,
	'evolution_rates': [1.02, 1.20, 1.23, 0.97, 0.88, 1.02, 1.20, 1.23, 0.97, 0.88, 1.02, 1.20, 1.23, 0.97, 0.88, 1.02, 1.20, 1.23, 0.97, 0.88, 1.02, 1.20, 1.23, 0.97, 0.88],
	'seq_length': '25000',
	'num_partitions': '25',
	'partitions': ['904', '779', '1447', '364', '1506','904', '779', '1447', '364', '1506','904', '779', '1447', '364', '1506','904', '779', '1447', '364', '1506','904', '779', '1447', '364', '1506'],

	### Multiprocessing settings ###
	# If set to 0, all CPUs are used
	'num_cpus': 2,
}
