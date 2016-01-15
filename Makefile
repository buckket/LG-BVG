.PHONY: clean clean-all download sort train

all: download sort train

clean-all:
	rm -f data/*.csv
	rm -f data/greetings/*
	rm -f data/information/*
	rm -f model/*

clean:
	rm -f data/greetings/*
	rm -f data/information/*
	rm -f model/*

download: data/bvg_ubahn.csv data/bvg_tram.csv data/bvg_bus.csv

sort:
	python sort.py

train:
	python train.py

data/%.csv:
	t timeline -e=replies -n=100000 --csv $(basename $(notdir $@)) > $@
