#!/usr/bin/env python3

def uefa_euro_2016(teams: str, scores: str) -> str:
	return f'At match {teams[0]} - {teams[1]}, {teams[0]} won!' if scores[0] > scores[1] else f'At match {teams[0]} - {teams[1]}, {teams[1]} won!' if scores[0] < scores[1] else f'At match {teams[0]} - {teams[1]}, teams played draw.'

print(uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]))
