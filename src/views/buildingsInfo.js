/////////////////////////////////////////////////////////////////////////////////
///////////////////// Set building information for the SVGs /////////////////////
/////////////////////////////////////////////////////////////////////////////////

export const campusBuildings = {
  ps: {bouygues: [0,1,2],
  breguet: [0,1,2,3,4],
  eiffel: [0,1,2,3,4]},
  metz: {metz: [-1,0,1,2,3]},
  rennes: {rennes: [1,2,3,4,5]}
}

export const latlngBuildings = {
  ps: {
    eiffel: {
      floor0: L.latLngBounds([
        [48.710893, 2.166501],
        [48.709698, 2.168707],
      ]),
      floor1: L.latLngBounds([
        [48.710893, 2.166501],
        [48.709698, 2.168707],
      ]),
      floor2: L.latLngBounds([
        [48.710893, 2.166503],
        [48.709694, 2.168707],
      ]),
      floor3: L.latLngBounds([
        [48.71089, 2.166501],
        [48.709698, 2.168706],
      ]),
      floor4: L.latLngBounds([
        [48.710878, 2.166494],
        [48.709687, 2.168701],
      ]),
    },
    bouygues: {
      floor0: L.latLngBounds([
        [48.709817, 2.166114],
        [48.70852, 2.168799],
      ]),
      floor1: L.latLngBounds([
        [48.709814, 2.166135],
        [48.708519, 2.168829],
      ]),
      floor2: L.latLngBounds([
        [48.709814, 2.166125],
        [48.708518, 2.168829],
      ]),
    },
    breguet: {
      floor0: L.latLngBounds([
        [48.709526, 2.162702],
        [48.707653, 2.16536],
      ]),
      floor1: L.latLngBounds([
        [48.709532, 2.162708],
        [48.707652, 2.165354],
      ]),
      floor2: L.latLngBounds([
        [48.70953, 2.162708],
        [48.70765, 2.165354],
      ]),
      floor3: L.latLngBounds([
        [48.709837, 2.163042],
        [48.707797, 2.164848],
      ]),
      floor4: L.latLngBounds([
        [48.709834, 2.163052],
        [48.707809, 2.164842],
      ]),
    },
  },
  metz: {
    metz:{
    "floor-1": L.latLngBounds([
      [49.10417, 6.219848],
      [49.102311, 6.221736],
    ]),
    floor0: L.latLngBounds([
      [49.104185, 6.220047],
      [49.10233, 6.221931],
    ]),
    floor1: L.latLngBounds([
      [49.10399, 6.220315],
      [49.103078, 6.221256],
    ]),
    floor2: L.latLngBounds([
      [49.104001, 6.220304],
      [49.103067, 6.221267],
    ]),
    floor3: L.latLngBounds([
      [49.103999, 6.220366],
      [49.103067, 6.221327],
    ]),}
  },
  rennes: {
    rennes:{
    floor1: L.latLngBounds([
      [48.124053, -1.624188], // + to up,- to right
      [48.126579, -1.622202], // + to up,- to right
    ]),
    floor2: L.latLngBounds([
      [48.124016, -1.624211], // + to up,- to right
      [48.126619, -1.622151], // + to up,- to right
    ]),
    floor3: L.latLngBounds([
      [48.125071, -1.62337], // + to up,- to right
      [48.126071, -1.62265], // + to up,- to right
    ]),
    floor4: L.latLngBounds([
      [48.125071, -1.62337], // + to up,- to right
      [48.126071, -1.62266], // + to up,- to right
    ]),
    floor5: L.latLngBounds([
      [48.125071, -1.62337], // + to up,- to right
      [48.126071, -1.62266], // + to up,- to right
    ]),}
  },
};
