#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name='John', job='Admin'):
        self._name = 'John'
        self._job = 'Admin'
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        # Case-insensitive match to make the test more flexible
        if any(value.casefold() == approved.casefold() for approved in APPROVED_JOBS):
            self._job = next(approved for approved in APPROVED_JOBS if value.casefold() == approved.casefold())
        else:
            print("Job must be in list of approved jobs.")
