# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2021 Taneli Hukkinen
# Licensed to PSF under a Contributor Agreement.

__all__ = ("loads", "load", "TOMLDecodeError")

from ._parser import TOMLDecodeError, load, loads

# Pretend this exception was created here.
TOMLDecodeError.__module__ = __name__


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
