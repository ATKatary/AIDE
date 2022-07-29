"""
aide models
"""
from django.db import models

class AbstractIDE(models.Model):
   """
   AF(ide_type, script, helper_scripts, 
      language, specifications, dependencies) = an abstract ide with that functions according to the 
                                                given_type. The ide’s primary language (and language of 
                                                the script and helperScripts is language).
   Abstract IDEs Flags
      - Static : executes programs, disallowing user interaction (e.g input() is excluded)
      - Interactive : allows for user interaction 
      - Optimized : optimizes script runtimes 
      - Contained : ide exists within a securely contained environment (e.g docker)

   Representation Invariant
      - specification must be enforced by the script
      - script and helper_scripts must be confirmed to be written in language
      - dependencies are all existing AbstractIDEs 
      - output type must be supported
            Note: if not supported, can only be used by same-language AbstractIDES
      - an AbstractIDE can’t depend on an AbstractIDE that depends on it (no circular logic)
   
   
   Representation Exposure
      - inherits from AbstractBaseuser
      - access allowed to all fields but they are all immutable
"""
##### Representation #####

#TODO: Representation

   def execute(self, command, obj = None) -> bool:
       """
       Executes program as if a blackbox, enforcing spec and outputting 
   
       Inputs
          :param permission: <str> referencing the functionality in question
          :param obj: <object> with the permission
   
       Outputs
          :returns: <bool> True if has the given permission on the obj, False otherwise
       """
       raise NotImplementedError

   def __str__(self) -> str:
       """ Override AbstractBaseUser.__str__() """
       raise NotImplementedError

