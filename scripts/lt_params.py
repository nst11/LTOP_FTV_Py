import ee
# Initialize the library.
ee.Initialize()

runParams = [{"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.75, "vertexCountOvershoot": 3, "preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.05, "bestModelProportion": 0.75,"minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.1, "bestModelProportion": 0.75,"minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 6, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 6},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 8, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 8},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 10, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 10},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.75, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 0.9, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.25, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.5, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 0.9, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.05, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.1, "bestModelProportion": 0.75, "minObservationsNeeded": 11},
             {"timeseries": ee.ImageCollection([]), "maxSegments": 11, "spikeThreshold": 1.0, "vertexCountOvershoot": 3,"preventOneYearRecovery": True, "recoveryThreshold": 1.0, "pvalThreshold": 0.15, "bestModelProportion": 0.75, "minObservationsNeeded": 11}]

