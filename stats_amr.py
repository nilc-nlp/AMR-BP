#!/usr/bin/python

import os
import penman
import collections
import sys

modal_verbs = ["possible-01", "likely-01", "obligate-01", "permit-01", "recommend-01", "prefer-01", "infer-01"]

named_entities = ["person", "family", "animal", "language", "nationality", "ethnic-group", "regional-group", "religious-group", "political-movement", "organization", "company", "government-organization", "military", "criminal-organization", "political-party", "market-sector", "school", "university", "research-institute", "team", "league", "location", "city", "city-district", "county", "state", "province", "territory", "country", "local-region", "country-region", "world-region", "continent", "ocean", "sea", "lake", "river", "gulf", "bay", "strait", "canal", "peninsula", "mountain", "volcano", "valley", "canyon", "island", "desert", "forest", "moon", "planet", "star", "constellation", "facility", "airport", "station", "port", "tunnel", "bridge", "road", "railway-line", "canal", "building", "theater", "museum", "palace", "hotel", "worship-place", "sports-facility", "market", "park", "zoo", "amusement-park", "event", "incident", "natural-disaster", "earthquake", "war", "conference", "game", "festival", "product", "vehicle", "ship", "aircraft", "aircraft-type", "spaceship", "car-make", "work-of-art", "picture", "music", "show", "broadcast-program", "publication", "book", "newspaper", "magazine", "journal", "natural-object", "award", "law", "court-decision", "treaty", "music-key", "musical-note", "food-dish", "writing-script", "variable", "program", "molecular-physical-entity", "small-molecule", "protein", "protein-family", "protein-segment", "amino-acid", "macro-molecular-complex", "enzyme", "nucleic-acid", "pathway", "gene", "dna-sequence", "cell", "cell-line", "species", "taxon", "disease", "medical-condition", "thing"]

def is_frameset(concept):
	fragments = concept.split("-")
	if len(fragments) > 1 and fragments[len(fragments)-1].isnumeric():
		return True
	else:
		return False


def get_top(sample, top_k=10):
	counter = collections.Counter(sample)
	top = [(x[0], x[1], x[1] * 100 /len(sample)) for x in counter.most_common(top_k)]
	return top


if __name__ == "__main__":


	fname = sys.argv[1]

	print("Loading Verb-Brasil framesets")
	framesets = []
	with open("verbo-brasil.dic","r", encoding="utf8") as f:
		framesets = [line.strip() for line in f]
	print(f'Verb-Brasil ({len(framesets)}) loaded')

	amrs = penman.load(fname)

	nodes = []
	instance_nodes = []
	edges = []
	tokens = []

	freq_concepts  = {"general concepts": 0, "named-entities": 0, "modal verbs": 0, \
					"amr-unknown": 0, "Verbo-Brasil framesets": 0, "constants": 0, \
					"negative":0, "special frames": 0}

	for amr in amrs:

		if "snt" in amr.metadata:
			tokens += [token.lower() for token in amr.metadata["snt"].split()]
		else:
			tokens += [token.lower() for token in amr.metadata["tok-pt"].split()]	

		nodes += [triple[2].lower() for triple in amr.triples \
						if triple[2] not in amr.variables() and triple[2] != "name"]
		edges += [triple[1] for triple in amr.triples \
						if triple[1] not in [":name", ":instance"]]


		for triple in amr.triples:
			if triple[1].startswith(":polarity") and triple[2] == "-":
				freq_concepts["negative"] = freq_concepts["negative"] + 1

		for triple in amr.instances():

			if triple[2] == "name":
				continue

			instance_nodes.append(triple[2].lower())

			if triple[2] in named_entities:
				freq_concepts["named-entities"] = freq_concepts["named-entities"] + 1
			elif triple[2] in modal_verbs:
				freq_concepts["modal verbs"] = freq_concepts["modal verbs"] + 1
			elif triple[2] == "amr-unknown":
				freq_concepts["amr-unknown"] = freq_concepts["amr-unknown"] + 1
			elif triple[2] in framesets:
				freq_concepts["Verbo-Brasil framesets"] = freq_concepts["Verbo-Brasil framesets"] + 1
			elif is_frameset(triple[2]):
				freq_concepts["special frames"] = freq_concepts["special frames"] + 1
			else:
				freq_concepts["general concepts"] = freq_concepts["general concepts"] + 1

	freq_concepts["constants"] = len(nodes) - len(instance_nodes) - freq_concepts["negative"]

	print("----------------------------------")
	print("Overview")
	print("----------------------------------")
	print(f'Number of instances: {len(amrs)}')
	print(f'Sentence tokens (total/unique):\t{len(tokens)}/{len(set(tokens))}')
	print(f'AMR Nodes (total/unique):\t{len(nodes)}/{len(set(nodes))}')
	print(f'AMR Instances (total/unique):\t{len(instance_nodes)}/{len(set(instance_nodes))}')
	print(f'AMR Edges (total/unique):\t{len(edges)}/{len(set(edges))}')

	print("----------------------------------")
	print("Concept details")
	print("----------------------------------")
	for key, value in freq_concepts.items():
		print(f'Number of {key}: {value}')

	print("----------------------------------")
	print("Most frequent edges and Verbo-Brasil framesets")
	print("----------------------------------")
	top_k = 10
	top_edges = get_top(edges, top_k)
	print(f'Top {top_k} edges')
	for edge, freq, percent in top_edges:
		print(f'{edge}\t{freq}\t{percent:.2f}%')

	print("----------------------------------")

	print(f'Top {top_k} Verbo-Brasil framesets')
	top_framesets = get_top([instance for instance in instance_nodes if is_frameset(instance)], top_k)
	for fset, freq, percent in top_framesets:
		print(f'{fset}\t{freq}\t{percent:.2f}%')


