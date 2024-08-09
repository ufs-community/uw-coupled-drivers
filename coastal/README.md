# Coastal

To execute this driver, in a conda environment where [`uwtools`](https://github.com/ufs-community/uwtools) is [installed](https://uwtools.readthedocs.io/en/stable/sections/user_guide/installation.html):

```
uw execute --module coastal.py --classname Coastal --task provisioned_rundir --config-file coastal.yaml --cycle 2024-08-05T12 --batch
```

Afterwards:

```
$ tree run
run
├── albedo.gr3 -> /path/to/data/albedo.gr3
├── bctides.in -> /path/to/data/bctides.in
├── datm_in
├── datm.streams
├── fd_ufs.yaml -> /path/to/model/tests/parm/fd_ufs.yaml
├── hgrid.gr3 -> /path/to/data/hgrid.gr3
├── hgrid.ll -> /path/to/data/hgrid.ll
├── INPUT
│   ├── data.nc -> /path/to/data/INPUT/wind_atm_fin_ch_time_vec_STR_fixed.nc
│   └── esmf_mesh.nc -> /path/to/data/INPUT/wind_atm_fin_ch_time_vec_ESMFmesh.nc
├── manning.gr3 -> /path/to/data/manning.gr3
├── model_configure -> /path/to/data/model_configure
├── noahmptable.tbl -> /path/to/data/noahmptable.tbl
├── param.nml
├── RESTART
├── runscript.coastal
├── station.in -> /path/to/data/station.in
├── ufs.configure -> /path/to/data/ufs.configure
├── vgrid.in -> /path/to/data/vgrid.in
├── watertype.gr3 -> /path/to/data/watertype.gr3
└── windrot_geo2proj.gr3 -> /path/to/data/windrot_geo2proj.gr3

2 directories, 19 files
```

To be run in a conda environment with [`uwtools`](https://github.com/ufs-community/uwtools) installed.

For development/testing, with conda active in your shell:

```
$ conda env create -f environment.yml
$ conda activate coastal
```
