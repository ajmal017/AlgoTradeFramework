from algotaf.backend.fileio import db_host, sensitive_data


TICKERS = ['abt', 'abbv', 'acn', 'ace', 'adbe', 'adt', 'aap',
           'aes', 'aet', 'afl', 'amg', 'a', 'gas', 'apd', 'arg',
           'akam', 'aa', 'agn', 'alxn', 'alle', 'ads', 'all', 'altr',
           'mo', 'amzn', 'aee', 'aal', 'aep', 'axp', 'aig', 'amt',
           'amp', 'abc', 'ame', 'amgn', 'aph', 'apc', 'adi', 'aon',
           'apa', 'aiv', 'amat', 'adm', 'aiz', 't', 'adsk', 'adp', 'an',
           'azo', 'avgo', 'avb', 'avy', 'bhi', 'bll', 'bac', 'bk', 'bcr',
           'bxlt', 'bax', 'bbt', 'bdx', 'bbby', 'brk-b', 'bby', 'blx',
           'hrb', 'ba', 'bwa', 'bxp', 'bsk', 'bmy', 'brcm', 'bf-b',
           'chrw', 'ca', 'cvc', 'cog', 'cam', 'cpb', 'cof', 'cah', 'hsic',
           'kmx', 'ccl', 'cat', 'cbg', 'cbs', 'celg', 'cnp', 'ctl', 'cern',
           'cf', 'schw', 'chk', 'cvx', 'cmg', 'cb', 'ci', 'xec', 'cinf',
           'ctas', 'csco', 'c', 'ctxs', 'clx', 'cme', 'cms', 'coh', 'ko',
           'cce', 'ctsh', 'cl', 'cmcsa', 'cma', 'csc', 'cag', 'cop', 'cnx',
           'ed', 'stz', 'glw', 'cost', 'cci', 'csx', 'cmi', 'cvs', 'dhi',
           'dhr', 'dri', 'dva', 'de', 'dlph', 'dal', 'xray', 'dvn', 'do',
           'dtv', 'dfs', 'disca', 'disck', 'dg', 'dltr', 'd', 'dov', 'dow',
           'dps', 'dte', 'dd', 'duk', 'dnb', 'etfc', 'emn', 'etn', 'ebay',
           'ecl', 'eix', 'ew', 'ea', 'emc', 'emr', 'endp', 'esv', 'etr',
           'eog', 'eqt', 'efx', 'eqix', 'eqr', 'ess', 'el', 'es', 'exc',
           'expe', 'expd', 'esrx', 'xom', 'ffiv', 'fb', 'fast', 'fdx', 'fis',
           'fitb', 'fslr', 'fe', 'fsiv', 'flir', 'fls', 'flr', 'fmc', 'fti',
           'f', 'fosl', 'ben', 'fcx', 'ftr', 'gme', 'gps', 'grmn', 'gd', 'ge',
           'ggp', 'gis', 'gm', 'gpc', 'gnw', 'gild', 'gs', 'gt', 'googl', 'goog',
           'gww', 'hal', 'hbi', 'hog', 'har', 'hrs', 'hig', 'has', 'hca', 'hcp',
           'hcn', 'hp', 'hes', 'hpq', 'hd', 'hon', 'hrl', 'hsp', 'hst', 'hcbk',
           'hum', 'hban', 'itw', 'ir', 'intc', 'ice', 'ibm', 'ip', 'ipg', 'iff',
           'intu', 'isrg', 'ivz', 'irm', 'jec', 'jbht', 'jnj', 'jci', 'joy', 'jpm',
           'jnpr', 'ksu', 'k', 'key', 'gmcr', 'kmb', 'kim', 'kmi', 'klac', 'kss',
           'krft', 'kr', 'lb', 'lll', 'lh', 'lrcx', 'lm', 'leg', 'len', 'lvlt',
           'luk', 'lly', 'lnc', 'lltc', 'lmt', 'l', 'low', 'lyb', 'mtb', 'mac',
           'm', 'mnk', 'mro', 'mpc', 'mar', 'mmc', 'mlm', 'mas', 'ma', 'mat',
           'mkc', 'mcd', 'mhfi', 'mck', 'mjn', 'mmv', 'mdt', 'mrk', 'met',
           'kors', 'mchp', 'mu', 'msft', 'mhk', 'tap', 'mdlz', 'mon', 'mnst',
           'mco', 'ms', 'mos', 'msi', 'mur', 'myl', 'ndaq', 'nov', 'navi',
           'ntap', 'nflx', 'nwl', 'nfx', 'nem', 'nwsa', 'nee', 'nlsn',
           'nke', 'ni', 'ne', 'nbl', 'jwn', 'nsc', 'ntrs', 'noc', 'nrg',
           'nue', 'nvda', 'orly', 'oxy', 'omc', 'oke', 'orcl', 'oi', 'pcar',
           'pll', 'ph', 'pdco', 'payx', 'pnr', 'pbct', 'pom', 'pep', 'pki',
           'prgo', 'pfe', 'pcg', 'pm', 'psx', 'pnw', 'pxd', 'pbi', 'pcl',
           'pnc', 'rl', 'ppg', 'ppl', 'px', 'pcp', 'pcln', 'pfg', 'pg',
           'pgr', 'pld', 'pru', 'peg', 'psa', 'phm', 'pvh', 'qrvo', 'pwr',
           'qcom', 'dgx', 'rrc', 'rtn', 'o', 'rht', 'regn', 'rf', 'rsg',
           'rai', 'rhi', 'rok', 'col', 'rop', 'rost', 'rlc', 'r', 'crm',
           'sndk', 'scg', 'slb', 'sni', 'stx', 'see', 'sre', 'shw', 'sial',
           'spg', 'swks', 'slg', 'sjm', 'sna', 'so', 'luv', 'swn', 'se',
           'stj', 'swk', 'spls', 'sbux', 'hot', 'stt', 'srcl', 'syk', 'sti',
           'symc', 'syy', 'trow', 'tgt', 'tel', 'te', 'tgna', 'thc', 'tdc',
           'tso', 'txn', 'txt', 'hsy', 'trv', 'tmo', 'tif', 'twx', 'twc',
           'tjk', 'tmk', 'tss', 'tsco', 'rig', 'trip', 'foxa', 'tsn',
           'tyc', 'ua', 'unp', 'unh', 'ups', 'uri', 'utx', 'uhs', 'unm',
           'urbn', 'vfc', 'vlo', 'var', 'vtr', 'vrsn', 'vz', 'vrtx', 'viab',
           'v', 'vno', 'vmc', 'wmt', 'wba', 'dis', 'wm', 'wat', 'antm', 'wfc',
           'wdc', 'wu', 'wy', 'whr', 'wfm', 'wmb', 'wec', 'wyn', 'wynn', 'xel',
           'xrx', 'xlnx', 'xl', 'xyl', 'yhoo', 'yum', 'zbh', 'zion', 'zts']

DB_NAME = 'algotaf'

USERNAME = sensitive_data.USERNAME
PASSWORD = sensitive_data.PASSWORD
HOSTNAME = db_host.DB_HOST
BACKUP_HOSTNAME = 'localhost'

TIMES = ['08:30', '08:31', '08:32', '08:33', '08:34', '08:35', '08:36', '08:37', '08:38', '08:39',
         '08:40', '08:41', '08:42', '08:43', '08:44', '08:45', '08:46', '08:47', '08:48', '08:49',
         '08:50', '08:51', '08:52', '08:53', '08:54', '08:55', '08:56', '08:57', '08:58', '08:59',
         '09:00', '09:01', '09:02', '09:03', '09:04', '09:05', '09:06', '09:07', '09:08', '09:09',
         '09:10', '09:11', '09:12', '09:13', '09:14', '09:15', '09:16', '09:17', '09:18', '09:19',
         '09:20', '09:21', '09:22', '09:23', '09:24', '09:25', '09:26', '09:27', '09:28', '09:29',
         '09:30', '09:31', '09:32', '09:33', '09:34', '09:35', '09:36', '09:37', '09:38', '09:39',
         '09:40', '09:41', '09:42', '09:43', '09:44', '09:45', '09:46', '09:47', '09:48', '09:49',
         '09:50', '09:51', '09:52', '09:53', '09:54', '09:55', '09:56', '09:57', '09:58', '09:59',
         '10:00', '10:01', '10:02', '10:03', '10:04', '10:05', '10:06', '10:07', '10:08', '10:09',
         '10:10', '10:11', '10:12', '10:13', '10:14', '10:15', '10:16', '10:17', '10:18', '10:19',
         '10:20', '10:21', '10:22', '10:23', '10:24', '10:25', '10:26', '10:27', '10:28', '10:29',
         '10:30', '10:31', '10:32', '10:33', '10:34', '10:35', '10:36', '10:37', '10:38', '10:39',
         '10:40', '10:41', '10:42', '10:43', '10:44', '10:45', '10:46', '10:47', '10:48', '10:49',
         '10:50', '10:51', '10:52', '10:53', '10:54', '10:55', '10:56', '10:57', '10:58', '10:59',
         '11:00', '11:01', '11:02', '11:03', '11:04', '11:05', '11:06', '11:07', '11:08', '11:09',
         '11:10', '11:11', '11:12', '11:13', '11:14', '11:15', '11:16', '11:17', '11:18', '11:19',
         '11:20', '11:21', '11:22', '11:23', '11:24', '11:25', '11:26', '11:27', '11:28', '11:29',
         '11:30', '11:31', '11:32', '11:33', '11:34', '11:35', '11:36', '11:37', '11:38', '11:39',
         '11:40', '11:41', '11:42', '11:43', '11:44', '11:45', '11:46', '11:47', '11:48', '11:49',
         '11:50', '11:51', '11:52', '11:53', '11:54', '11:55', '11:56', '11:57', '11:58', '11:59',
         '12:00', '12:01', '12:02', '12:03', '12:04', '12:05', '12:06', '12:07', '12:08', '12:09',
         '12:10', '12:11', '12:12', '12:13', '12:14', '12:15', '12:16', '12:17', '12:18', '12:19',
         '12:20', '12:21', '12:22', '12:23', '12:24', '12:25', '12:26', '12:27', '12:28', '12:29',
         '12:30', '12:31', '12:32', '12:33', '12:34', '12:35', '12:36', '12:37', '12:38', '12:39',
         '12:40', '12:41', '12:42', '12:43', '12:44', '12:45', '12:46', '12:47', '12:48', '12:49',
         '12:50', '12:51', '12:52', '12:53', '12:54', '12:55', '12:56', '12:57', '12:58', '12:59',
         '13:00', '13:01', '13:02', '13:03', '13:04', '13:05', '13:06', '13:07', '13:08', '13:09',
         '13:10', '13:11', '13:12', '13:13', '13:14', '13:15', '13:16', '13:17', '13:18', '13:19',
         '13:20', '13:21', '13:22', '13:23', '13:24', '13:25', '13:26', '13:27', '13:28', '13:29',
         '13:30', '13:31', '13:32', '13:33', '13:34', '13:35', '13:36', '13:37', '13:38', '13:39',
         '13:40', '13:41', '13:42', '13:43', '13:44', '13:45', '13:46', '13:47', '13:48', '13:49',
         '13:50', '13:51', '13:52', '13:53', '13:54', '13:55', '13:56', '13:57', '13:58', '13:59',
         '14:00', '14:01', '14:02', '14:03', '14:04', '14:05', '14:06', '14:07', '14:08', '14:09',
         '14:10', '14:11', '14:12', '14:13', '14:14', '14:15', '14:16', '14:17', '14:18', '14:19',
         '14:20', '14:21', '14:22', '14:23', '14:24', '14:25', '14:26', '14:27', '14:28', '14:29',
         '14:30', '14:31', '14:32', '14:33', '14:34', '14:35', '14:36', '14:37', '14:38', '14:39',
         '14:40', '14:41', '14:42', '14:43', '14:44', '14:45', '14:46', '14:47', '14:48', '14:49',
         '14:50', '14:51', '14:52', '14:53', '14:54', '14:55', '14:56', '14:57', '14:58', '14:59', '15:00']
