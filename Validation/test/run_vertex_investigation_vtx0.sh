#!/bin/bash

path_to_dir=/eos/cms/store/group/phys_higgs/cmshgg/gallim/
out_dir=VertexInvestigation_vtx0

fggRunJobs.py --load jobs_vertex_investigation.json -x cmsRun vertex_investigation_vtx0.py -d ${out_dir} maxEvents=-1 useAAA=1 -q tomorrow --make-light-tarball --stage-to=$path_to_dir$out_dir -n 500 --no-copy-proxy -H
#fggRunJobs.py --load jobs_vertex_investigation.json -x cmsRun vertex_investigation_vtx0.py -d ${out_dir} maxEvents=1000 useAAA=1 -q longlunch --make-light-tarball --stage-to=$path_to_dir$out_dir -n 1 --no-copy-proxy -H
