insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("ExecDest","String",100,"The destination name the order is to be routed too. Not relevant on the Core",1);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("StartTime","Time",9242,"the time to start working and order represented in UTC",2);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("EndTime","Time",9126,"the time to stop working and order represented in UTC",3);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Price","Price",44,"the price represented as a long",4);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Display Quantity","Integer",111,"The maximum quantity to display to the floor",5);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Style","String",9245,"Experts/Rules - PASSIVE, NORMAL, AGGRESSIVE, or, for US only, SUPER-AGGRESSIVE",6);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("TargetParticipationRate","Float",9243,"1-100 in percent, Newport 3 Rules use PCTVOLUME",7);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("PctVolume","Float",7502,"1-100 in percent, used by Newport 3 Rules, Experts interprets this tag to mean TARGET_PARTICIPATION_RATE",8);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("MaxPctVolume","Float",9244,"0-100 in percent",9);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("MinPctVolume","Float",9848,"0-100 in percent",10);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("LimitType1","String",9043,"LAST - Last price as limit None AVG - Average price as limit None VWAP - VWAP as limit (from arrival time) None REL - Relative return limit price (US only) Percent STR - Straight return limit price (US only) Percent MKT - Market adjusted limit price (US only) Price QUOTE - Aggressive quote return limit price (in bps) (US only) Integer",11);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("LimitSymbol","String",9055,"Any valid US Symbol",12);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("LimitTime","Time",9056,"a time represented in UTC",13);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("LimitValue","Float",9057,"Price or Percent based on LimitType",14);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("IWouldPrice","Price",9044,"(US Only)",15);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Tilt","Integer",9127,"-100 to 100 (default is 0) (US Only)",16);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("IncludeClose","Char",9111,"Y/N",17);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Benchmark","String",9541,"OPEN or CLOSE (mutually exclusive with BenchmarkPrice)",18);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("BenchmarkPrice","Float",9542,"(mutually exclusive with Benchmark)",19);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("MustComplete","Char",9112,"Y/N (US Only)",20);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("AuctionParticipation","Char",9248,"Y/N (EU & AS)",21);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("AggregrationTag","String",9066,"10-character max unique name",22);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("CashTarget","Float",9767,"Positive for raise cash (sell) Negative for spend cash (buy)",23);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("RaiseLimit","Float",9768,"Amount you’re willing to trade in a positive direction above the cash constraint. Narrower ranges may hinder trading behavior.",24);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("SpendLimit","Float",9769,"Amount you’re willing to trade in a negative direction below the cash constraint. Narrower ranges may hinder trading behavior.",25);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("InitializationMethod2","String",9770,"IMM - Immediately OPT - Optimally BSB - % Dollar balanced (All Buys vs All Sells) SBS - % Dollar balanced (All Buys vs Sells vs Short Sells) TIME - Time balanced",26);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Investor ID","String",9584,"QFII ID for Taiwan and Korea",27);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Rule80A","Char",47,"A, K, or J,",28);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("TriggerValue","Float",9515,"4-digit precision; target spread ratio or log ratio",29);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("PacingFactor","Float",9486,"0-100",30);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("InitSide","String",9624,"“Buy”, ”Sell”, or ”SellShort”",31);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("UseSellPrice","String",9331,"“BID”, “ASK”, “LAST”",32);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("UseBuyPrice","String",9330,"“BID”, “ASK”, “LAST”",33);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("TriggerMethod","String",9514,"RBS - Ratio (B/S) RSB - Ratio (S/B) SBS - Spread (B-S) SSB - Spread (S-B) LBS - Log Ratio (ln(B/S)) LSB - Log Ratio (ln(S/B))",34);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("TriggerDirection","String",9516,"“GT” or “LT”",35);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("BuyTermsRatio","Float",9399,"4-digit precision; default value should be set to 1",36);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("SellTermsRatio","Float",9407,"4-digit precision; default value should be set to 1",37);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("BuyTermsCash","Price",9400,"Default value should be set to 0",38);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("SellTermsCash","Price",9408,"Default value should be set to 0",39);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("WorkPassiveSide","Char",9567,"Y/N",40);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("WorkInside","Char",9568,"Y/N",41);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("IOCInitSide","Char",9569,"Y/N",42);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("MaxSliceValue","Price",9566,"Maximum allowed to submit at any one point in time; should be a positive, non-zero value",43);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("MaintainShareRatio","Char",9321,"Y/N",44);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("ReviseIntervalMin","Integer",9532,"Minimum of random interval of time to wait between revisions of order currently exposed",45);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("ReviseIntervalMax","Integer",9533,"Maximum of random interval of time to wait between revisions of order currently exposed",46);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("ReloadIntervalMin","Integer",9534,"Minimum of random interval of time to wait between submissions to destination",47);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("ReloadIntervalMax","Integer",9535,"Maximum of random interval of time to wait between submissions to destination",48);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("DisplayQuoteMultiple","Float",9536,"quoted price",49);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("AlwaysMorePassive","Char",9508,"Y/N",50);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("TicksAggressive","Integer",9586,"Number of ticks over which to adjust the price aggressively",51);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("PercentAggressive","Float",9580,"Percent to adjust the required price aggressively",52);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("IncludeAllVol","Char",9540,"Y/N",53);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Urgency","Integer",9061,"0-10",54);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Price Aggressiveness","Integer",9045,"0-10",55);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Risk Tolerance","Integer",9101,"0-10",56);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("UseOptimalPartRate","Char",9859,"Y/N",57);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("AutoCalcRate","Char",9853,"Y/N",58);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("PeriodicAutoCalcRate","Char",9854,"Y/N",59);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("MinCrossFillQty","Integer",110,"The minimum amount of shares the order can execute at",60);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("BlockSizeToIgnore","Integer",9129,"Ignore any block size greater than X when calculating volume consideration",61);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("CBX Elligable","Char",7676,"Y/N",62);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Amortize","Char",7615,"Y/N",63);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("AuctionCatchup","Char",7737,"Y/N",64);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("AverageDown","Char",7631,"Y/N",65);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("CBX_Display","String",7670,"Free form String with CBX display instructions for Algos",66);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("CBX_Hidden","Char",7702,"Y/N",67);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("DisableOffExchange","Char",7674,"Y/N",68);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("ECN_Display","Char",7675,"Y/N",69);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("ECN_Only'","Char",9113,"Y/N",70);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("ExtendedReporting","Char",7647,"Y/N",71);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("IDX_Eligible","Char",7507,"Y/N",72);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("IgnoreMarketDataStatus","Char",7623,"Y/N",73);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("IndexArbType","Char",7739,"Y/N",74);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("IsMOC","Char",7624,"Y/N",75);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("IsMOO","Char",7733,"Y/N",76);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("IsTimedRelease","Char",7751,"Y/N",77);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("IsTWAP","Char",7602,"Y/N",78);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("JX_Eligible","Char",7685,"Y/N",79);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("LegacyDeskType","String",966,"if value is CUSTOMER then set 6218=Y otherwise 6218=N",80);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("OpenEligible","Char",7679,"Y/N",81);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("OrderVisibility","Char",7782,"VTMFOrderVisibility values B=BuySide, S=SellSide, A=All, M=MarketMaker, D=Dark",82);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("PrimaryDisplay","String",9130,"Free form String",83);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("RiskAversion","String",7703,"Free form String",84);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Rounding","String",7634,"Free form String",85);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Schedule","String",7633,"Free form String",86);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("ScheduleDiscretion","String",7682,"Free form String",87);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("SMRTReroutable","Char",9303,"R - Allow Reroute, N - Don’t Allow Reroute",88);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("TrackingDiscretion","String",7683,"Free form String",89);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("TSX_Anonymous","Char",6761,"Y/N",90);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("UseClientId","Char",976,"Y/N",91);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("UseDynamicRateCalc","Char",9205,"Y/N",92);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("WorkActively","Char",7658,"Y/N",94);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("ExPartnerID","Char",8019,"The Exchange PartnerID",95);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("ExIgnoreWarning","Char",8020,"Y/N",96);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Paired Symbol","String",7750,"This is where the user should enter the symbol that they wish to track. They can enter INDEX if they want to pair against a benchmark index for the stock. We will expect InetSymbol for now. We may want to change this in the future to convert client's symbology.",97);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Paired Symbol Benchmark","String",7755,"This is where the client can specify a benchmark for the paired symbol for the rule to track to. The options are as follows: - Ask - Bid -Floating Last -Floating VWAP -Last Trade -Market -Mid Price -None -Primary -VWAP",98);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Expert Override Volume Pattern","String",9543,"If specified, this field needs to match the ID Source delivered in tag 22. If the client delivers an invalid symbol, the Expert should reject the order back to the client. Experts will use this field as a reference symbology profile.",99);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Target Completion","Integer",7783,"Target Completion for Asian Algos.",100);
insert into fix (fix_name,fix_type,fix_tag,fix_notes,vtmf_id) values ("Sweep Book","Boolean",7784,"Sweep Book for Asian Algos.",101);