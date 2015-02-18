package beatProgramming.BetData;

public enum Liga {
	//Ligas de cada pais
	BBVA("/primera"),
	ADELANTE("/segunda"),
	PREMIER("/premier"),
	CHAMPIONSHIP("/championship"),
	SERIE_A("/serie_a"),
	SERIE_B("/serie_b"),
	BUNDESLIGA("/bundesliga"),
	LIGUE_1("/ligue_1"),
	PORTUGUESA("/portugal"),
	HOLANDESA("/holanda"),
	ARGENTINA("/primera_division_argentina"),
	RUSA("/rusia"),
	TURCA("/turquia"),
	BELGA("/belgica"),
	ESCOCESA("/escocia"),
	GRIEGA("/gercia"),
	AUSTRIACA("/austria"),
	UCRANIANA("/liga_ucraniana"),
	CROATA("/croacia"),
	
	//Competiciones
	CHAMPIONS("/champions"),
	UEFA("/uefa"),
	COPA_DEL_REY("/copa_del_rey"),
	FA_CUP("/fa_cup"),
	COPPA_ITALIA("/coppa_italia"),
	COPA_FRANCIA("/copa_de_francia");
	
	
	private final String path;
	
	private Liga(String path) {
		this.path = path;
	}
	
	public String getPath() {
		return path;
	}
	
}
