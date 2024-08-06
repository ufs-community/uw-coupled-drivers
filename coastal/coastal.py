from iotaa import asset, task, tasks
from uwtools.api.cdeps import CDEPS
from uwtools.api.driver import DriverCycleBased
from uwtools.api.file import link
from uwtools.api.logging import use_uwtools_logger
from uwtools.api.schism import SCHISM

use_uwtools_logger()


class Coastal(DriverCycleBased):
    """
    A driver for the Coastal App coupled executable.
    """

    @task
    def linked_files(self):
        """
        Link data files into the run directory.
        """
        links = self.config["links"]
        path = lambda fn: self.rundir / fn
        yield "Linked files"
        yield [asset(path(fn), path(fn).is_file) for fn in links.keys()]
        yield None
        link(config=links, target_dir=self.rundir)

    @tasks
    def provisioned_rundir(self):
        """
        Provision the run directory with all required content.
        """
        cdeps = CDEPS(config=self.config_full, cycle=self.cycle, controller=self._driver_name)
        schism = SCHISM(config=self.config_full, cycle=self.cycle, controller=self._driver_name)
        yield "Provisioned run directory"
        yield [
            cdeps.atm_nml(),
            cdeps.atm_stream(),
            schism.namelist_file(),
            self.linked_files(),
            self.runscript(),
        ]

    @property
    def _driver_name(self):
        return "coastal"
