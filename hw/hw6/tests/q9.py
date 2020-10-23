test = {   'name': 'q9',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> def rmse(predicted, actual):\n'
                                               '...     return np.sqrt(np.mean((actual - predicted)**2));\n'
                                               '>>> \n'
                                               ">>> training_data_fm = pd.read_csv('ames_train_cleaned.csv');\n"
                                               '>>> X_train_fm, y_train_fm = process_data_fm(training_data_fm);\n'
                                               '>>> \n'
                                               '>>> _ = final_model.fit(X_train_fm, y_train_fm);\n'
                                               '>>> y_predicted_train_fm = final_model.predict(X_train_fm);\n'
                                               '>>> training_rmse_fm = rmse(y_predicted_train_fm, y_train_fm);\n'
                                               '>>> \n'
                                               '>>> training_rmse_fm <= 38000\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> def rmse(predicted, actual):\n'
                                               '...     return np.sqrt(np.mean((actual - predicted)**2));\n'
                                               '>>> \n'
                                               ">>> training_data_fm = pd.read_csv('ames_train_cleaned.csv');\n"
                                               ">>> test_data_fm = pd.read_csv('ames_test_cleaned.csv');\n"
                                               '>>> \n'
                                               '>>> X_train_fm, y_train_fm = process_data_fm(training_data_fm);\n'
                                               '>>> X_test_fm, y_test_fm = process_data_fm(test_data_fm);\n'
                                               '>>> \n'
                                               '>>> _ = final_model.fit(X_train_fm, y_train_fm);\n'
                                               '>>> y_predicted_train_fm = final_model.predict(X_train_fm);\n'
                                               '>>> y_predicted_test_fm = final_model.predict(X_test_fm);\n'
                                               '>>> \n'
                                               '>>> training_rmse_fm = rmse(y_predicted_train_fm, y_train_fm);\n'
                                               '>>> test_rmse_fm = rmse(y_predicted_test_fm, y_test_fm);\n'
                                               '>>> \n'
                                               '>>> test_rmse_fm <= 39000\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
