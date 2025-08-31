# Changelog

All notable changes to this project will be documented in this file, because even for small projects, changelogs help, for myself, for collaborators and especially for others following along ;)

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html), although there won


## [0.0.1] - 2025-08-30
 * set up repo with `LICENSE`, `README.md`, `CHANGELOG.md`
 * get python project structure in with ./rankedleague and ./tests
 * start with a simple `Team` model in `domain.py` (DDD, no naked primitives), with hashing and equality so we can use it later
 * set up pytest, a few tests on the `Team` model, starting with 100% coverage 

## [0.0.2] - 2025-08-31
 * create Result model

## WIP
 * Calculate league points for result

## Todo
 * League table, adding results, ordering
 * Results from file
 * League table to file

## Maybes
 * also support stdin/stdout