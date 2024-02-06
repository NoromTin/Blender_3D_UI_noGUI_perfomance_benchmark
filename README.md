# Blender3D_gui_backend_perfomance_test
Perfomance test for Blender3D UI without GUI (mainly for particle system)
Multiprocessing core scalability.

Contain tests:
1. particle_movement    - Spreading particles in empty space
2. particle_collision   - Spreading and continously reflecting in compressed conditions (sphere)
3. empty_play           - just playing in empty scene

Requirements:
1. Some .py file editing experience
1. Tested with Blender 3.5, 4.0 versions
2. 400mb ram per logical core (num of cores used in test can be limited with configuration part)

Quick start:
1. check os python 3 libs
1. Win: pip install psutil py-cpuinfo
1. linux: apt install python3-pip && pip install psutil py-cpuinfo
2. check blender python libs
2. [blender dir] \ [blender ver] \python\bin\python -m pip install [libs for scene_*.py]
2. Win: "c:\Program Files\Blender Foundation\Blender 3.5\3.5\python\bin\python -m pip install [libs for scene_*.py]
3. configure bench settings in file bench_start.py (blender path, MP usage, info string vars for result file)
4. run bench_start_win.py
5. read result in console or csv
6. you could send result to aninelo@gmail.com OR push it to this rep with your branch

Result RAW structure:
1. os_type                  - string
2. test_type                - string
3. mp_type                  - string
4. num_thread per instance  - int (1 for bench_mp_type ='mp')
5. num instances            - int (1 for bench_mp_type ='thread')
6. list of tuples           - float [(time_start, time_end),] in seconds for every instance

Result analisys structure:
1. cpu_name     - string [large cpu name]                           (autodetected, from cpuinfo import get_cpu_info)
2. hardware     - string [hardware platform (brand, mb, ram etc.)]  (added manually, hardware var in bench_start.py)
3. bench_env    - string ['bare','vm*']                             (added manually, 'bare' for real host, 'vm [brand] [hypervisor os] [hypervisor cpu if needed]' )
4. os_type      - string ['Win','Lnx','Mac']                        (autodetected, from sys import platform)
5. os_release   - string [Major os version]                         (autodetected, import platform, platform.release())
6. os_version   - string [Detailed os version]                      (autodetected, import platform, platform.version())
7. blender_version - string [Blender app major version]             (autodetected, scene*.py file, import bpy, bpy.app.version_string)
8. test_type    - string ['particle_movement','particle_collision','empty_play'] (autodetected, test_type_list)
4. mp_type      - string ['mp','mt']                                (autodetected, mp_type_list)
5. core_num     - int    [number of cores used in current test]     (autodetected, HT included logical cores)
6. cpu_rating   - float  [cpu compute rating in this test]          (calculated, all tests complexity needed to be scale for around the same one core cpu power)
7. core_rating  - float  [core efficiency]                          (calculated)
8. avg_time     - float  [average time, sec]                        (calculated)
9. med_time     - float  [mediana time, sec]                        (calculated)
10. min_time    - float  [minimal time, sec]                        (calculated)
11. max_time    - float  [maximum time, sec]                        (calculated)


TODO solid and term refactoring
TODO Make online result collector, like : https://www.cgdirector.com/blender-benchmark-results-updated-scores/
TODO List to dict, pythonic way

GOOD Linux starter bench_start_linux.py or unified
GOOD Complete Main test type №2 file(Collisions)
GOOD MacOS starter
GOOD READY csv export
GOOD Warming up cpu to get more honest result
GOOD Conclusion analysys
GOOD Blender version


