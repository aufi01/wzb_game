prelim_matrix= np.matrix("1 2; 3 4; 5 6; 6 7; 8 9; 10 11; 12 13; 14 15")
var_ordinal = {'claimed_content':['richkid', 'poorkid', 'sunset', 'noanswer']}
var_cardinal = ['donation']
var_names = ['donation', 'claimed_content']

sample_size = len(players)
num_covariates = len(var_names)

def axess_data(player_nr, var_name, players=players):
    temp = eval("players[player_nr]." + var_name)
    return temp


# Store covariates in matrix
prelim_matrix = np.matrix([[axess_data(i, j) for i in range(len(players))] for j in var_names])
final_matrix = np.zeros((sample_size,1)) # will be later changed to numpy matrix


if var_cardinal is None:
    var_cardinal = list()
    for name in var_names:
        if not name in var_ordinal:
            if isinstance(axess_data(0, name), str):
                var_cardinal.append(name)


temp_col = prelim_matrix[:,i]
if var_names[i] in var_cardinal:
    df = pd.DataFrame(temp_col, columns=['temp'])
    df_temp = pd.get_dummies(df['temp'])
    mat_temp = df_temp.as_matrix(columns=None)
    final_matrix = np.concatenate(final_matrix, mat_temp[:, -0])