---
id: github:teqplay/portreporter-backend:issue:941
source: github
type: issue
repo: teqplay/portreporter-backend
number: 941
title: Feat/Matchingnominationportcallfunction
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/941
labels: []
explicit_links: []
---
# Issue #941: Feat/Matchingnominationportcallfunction

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/941  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [68d99a223cd1...f94c0008dd54](https://github.com/teqplay/portreporter-backend/compare/68d99a223cd1...f94c0008dd54)
**Merge commit:** [f94c0008dd54](https://github.com/teqplay/portreporter-backend/commit/f94c0008dd54)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop, Former user
**Source Branch:** [feat/matchingNominationPortcallFunction](https://github.com/teqplay/portreporter-backend/tree/feat/matchingNominationPortcallFunction)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:39.645935+00:00
**Status:** MERGED

* \[ https://trello.com/c/o4yiDi8S \] : Adding two functions to match portcalls and nomination:

    * PortcallLogic.getMatchingPortCallByNomination\(Nomination\): Portcall? - \(declared in the PortcallLogic\) > To be used to LOCATE the best matching Portcall
    * NominationLogic.getMatchingNominationByPortcall\(Portcall\): Nomination? - \(declared in the NominationLogic\) > to be used to LOCATE the best matching Nomination
    

    Additionally, a set of methods in both logics have been added to easy its usage: - NominationLogic.updateByMatchingPortcall\(Portcall\):Nomination? > To be used to UPDATE a nomination's portcallId with the the best matching Portcall - NominationLogic.resetPortCallId\(String\):Nomination? > To be used to RESET a nomination's portcallId \(to null\) in the event of cancelling a portcall



    As well as the corresponding unitTests \(so far they can be done\).


* \[ https://trello.com/c/o4yiDi8S \] : Removing a leaked code grammar typo
* \[ https://trello.com/c/o4yiDi8S \] : And adjusting a variable in related unitTests


