//c++

#include <string>  
#include <sstream>
#include <fstream>
#include <cassert>    
#include <iostream>
#include <math.h>

// Boost
#include <boost/scoped_ptr.hpp>



// QUESO
#include <queso/GslVector.h>
#include <queso/GslMatrix.h>
#include <queso/BoxSubset.h>
#include <queso/InterpolationSurrogateIOASCII.h>
#include <queso/LinearLagrangeInterpolationSurrogate.h>

/*
namespace QUESO
{
  class BaseEnvironment;

  template<class V, class M>
  class InterpolationSurrogateIOASCII;

  template<class V, class M>
  class LinearLagrangeInterpolationSurrogate;
}
*/


template<class V, class M>
class flamespeed_values
{
protected:
  
  QUESO::LinearLagrangeInterpolationSurrogate<V,M>* _flame_surrogate_20;
  QUESO::LinearLagrangeInterpolationSurrogate<V,M>* _flame_surrogate_28;
  QUESO::LinearLagrangeInterpolationSurrogate<V,M>* _flame_surrogate_40;
	QUESO::LinearLagrangeInterpolationSurrogate<V,M>* _flame_surrogate_46;
  QUESO::LinearLagrangeInterpolationSurrogate<V,M>* _flame_surrogate_53;
  QUESO::LinearLagrangeInterpolationSurrogate<V,M>* _flame_surrogate_75;
	QUESO::LinearLagrangeInterpolationSurrogate<V,M>* _flame_surrogate_100;
	 
	 
	 
	 QUESO::InterpolationSurrogateIOASCII<V,M>* _interp_20;
	 QUESO::InterpolationSurrogateIOASCII<V,M>* _interp_28;
	 QUESO::InterpolationSurrogateIOASCII<V,M>* _interp_40;
	 QUESO::InterpolationSurrogateIOASCII<V,M>* _interp_46;
	 QUESO::InterpolationSurrogateIOASCII<V,M>* _interp_53;
	 QUESO::InterpolationSurrogateIOASCII<V,M>* _interp_75;
	 QUESO::InterpolationSurrogateIOASCII<V,M>* _interp_100;
 // Instantiate GSL version of this class
 // template class QUESO::LinearLagrangeInterpolationSurrogate<QUESO::GslVector,QUESO::GslMatrix> flame_surrogate;
public:

  flamespeed_values(const char * prefix, const QUESO::VectorSet<V, M> & domain,
      const V & observations, const V & covariance, QUESO::FullEnvironment& env )
  {
  
   std::string flame_20_filename = "flamespeed_20.dat";     
   std::string flame_28_filename = "flamespeed_28.dat";
   std::string flame_40_filename = "flamespeed_40.dat";
   std::string flame_46_filename = "flamespeed_46.dat";
   std::string flame_53_filename = "flamespeed_53.dat";
   std::string flame_75_filename = "flamespeed_75.dat";
   std::string flame_100_filename = "flamespeed_100.dat";
  
  
  
  
  
  _interp_20 = new QUESO::InterpolationSurrogateIOASCII<V,M>;
  _interp_28 = new QUESO::InterpolationSurrogateIOASCII<V,M>;
  _interp_40 = new QUESO::InterpolationSurrogateIOASCII<V,M>;
  _interp_46 = new QUESO::InterpolationSurrogateIOASCII<V,M>;
  _interp_53 = new QUESO::InterpolationSurrogateIOASCII<V,M>;
  _interp_75 = new QUESO::InterpolationSurrogateIOASCII<V,M>;
  _interp_100 =new QUESO::InterpolationSurrogateIOASCII<V,M>;
  
  
 
  _interp_20->read( flame_20_filename, env, "param_");
  _interp_28->read( flame_28_filename, env, "param_");
  _interp_40->read( flame_40_filename, env, "param_");
  _interp_46->read( flame_46_filename, env, "param_");  
  _interp_53->read( flame_53_filename, env, "param_");
  _interp_75->read( flame_75_filename, env, "param_");
  _interp_100->read( flame_100_filename, env, "param_");
  
   /*
   data_reader.read( "flamespeed.dat", env, "param_" );
   data_reader.read( "flamespeed_100.dat", env, "param_" );
*/
  // Grab a reference to the data built in the reader
//  const QUESO::InterpolationSurrogateData<V,M>& data = data_reader.data();

  // The reader read in the data, so now we can give the data
  // to the interpolation surrogate. This object can now be used in a likelihood
  // function for example. Here, we just illustrate calling the surrogate model
  // evaluation.
  

  _flame_surrogate_20 = new QUESO::LinearLagrangeInterpolationSurrogate<V,M> ( _interp_20->data() ); 
  _flame_surrogate_28 = new QUESO::LinearLagrangeInterpolationSurrogate<V,M> ( _interp_28->data() );
  _flame_surrogate_40 = new QUESO::LinearLagrangeInterpolationSurrogate<V,M> ( _interp_40->data() );
  _flame_surrogate_46 = new QUESO::LinearLagrangeInterpolationSurrogate<V,M> ( _interp_46->data() );
  _flame_surrogate_53 = new QUESO::LinearLagrangeInterpolationSurrogate<V,M> ( _interp_53->data() );
  _flame_surrogate_75 = new QUESO::LinearLagrangeInterpolationSurrogate<V,M> ( _interp_75->data() );
  _flame_surrogate_100 = new QUESO::LinearLagrangeInterpolationSurrogate<V,M> ( _interp_100->data() );
  
  }

  virtual ~flamespeed_values()
  {
  
  
     
     delete  _flame_surrogate_20;
     delete  _flame_surrogate_28;
     delete  _flame_surrogate_40;
     delete  _flame_surrogate_46;
     delete  _flame_surrogate_53;
     delete  _flame_surrogate_75;
     delete  _flame_surrogate_100;
     
     

      delete _interp_20;
      delete _interp_28;
      delete _interp_40;
      delete _interp_46;
      delete _interp_53;
      delete _interp_75;
      delete _interp_100;
  }

  virtual void evaluateModel(const V& param_values, V& model_output ) const
  {
   

   double value_20 = _flame_surrogate_20->evaluate(param_values);
   double value_28 = _flame_surrogate_28->evaluate(param_values);
   double value_40 = _flame_surrogate_40->evaluate(param_values);
   double value_46 = _flame_surrogate_46->evaluate(param_values);
   double value_53 = _flame_surrogate_53->evaluate(param_values);
   double value_75 = _flame_surrogate_75->evaluate(param_values);
   double value_100 = _flame_surrogate_100->evaluate(param_values);
  
 
  
    // Evaluate model and fill up the m_modelOutput member variable
    for (unsigned int i = 0; i < model_output.sizeLocal(); i++) {
      
      
      model_output[0] = value_20;
      model_output[1] = value_28;
      model_output[2] = value_40;
      model_output[3] = value_46;    
      model_output[4] = value_53;
      model_output[5] = value_75;
      model_output[6] = value_100;
      
    }
  }
};


int main(int argc, char* argv[])
{

  //************************************************
  // Initialize environments
  //************************************************
  MPI_Init(&argc,&argv);

  {
 
  QUESO::FullEnvironment env(MPI_COMM_WORLD, argv[1], "", NULL);
  QUESO::VectorSpace<QUESO::GslVector, QUESO::GslMatrix> paramSpace(env, "param_", 1, NULL);
  QUESO :: GslVector paramMinValues ( paramSpace . zeroVector ());
  QUESO :: GslVector paramMaxValues ( paramSpace . zeroVector ());

  // the pre-exponential factor variation of O + O3 [=] O2 + O2 reaction(3)
    
  paramMinValues [0] = 0;
  paramMaxValues [0] = 70;
   
   


  QUESO::BoxSubset<QUESO::GslVector, QUESO::GslMatrix> paramDomain("param_",paramSpace, paramMinValues, paramMaxValues);


// Set up observation space
    QUESO::VectorSpace<QUESO::GslVector, QUESO::GslMatrix> obsSpace(env,
								    "obs_", 7, NULL);

    // Fill up observation vector
    QUESO::GslVector observations(obsSpace.zeroVector());
 		 observations[0] = 0.182;
     observations[1] = 0.522;
 		 observations[2] = 1.25;
 		 observations[3] = 1.66;
 		 observations[4] = 2.1; 
 		 observations[5] = 3.31;
 		 observations[6] = 4.75;
 
 
 
	QUESO::GslVector covariance(obsSpace.zeroVector()); 
 		covariance[0] = 0.00033124; 
 		covariance[1] = 0.00272484; 
 		covariance[2] = 0.015625; 
 		covariance[3] = 0.027556; 
 		covariance[4] = 0.0441; 
 		covariance[5] = 0.109561; 
 		covariance[6] = 0.225625; 


QUESO::GslVector params(paramSpace . zeroVector ());
 QUESO::GslVector output(obsSpace.zeroVector());

    flamespeed_values<QUESO::GslVector,QUESO::GslMatrix>
      surrogate_model("llhd_", paramDomain, observations, covariance,env  );

    // Read in points at which to evaluate the model
    std::ifstream input;
    std::vector<double> E3;
    E3.reserve(1e7);

    input.open("testdata.dat");

    std::cout << "Input is " << input.good() << std::endl;
    std::cout << "Reading Data!" << std::endl;
    while( input.good() )
      {
        double  E3N;

        input >> E3N;

        E3.push_back(E3N);
      }
    std::cout << "E3 size = " << E3.size() << std::endl;
    input.close();
    std::cout << "Done reading data!" << std::endl;

    std::ofstream ofile;
    ofile.open("modelpoints.dat");

    for( unsigned int i = 0; i < E3.size(); i++)
      {
        params[0] = E3[i];
        surrogate_model.evaluateModel(params, output);

        for( unsigned int j = 0; j < output.sizeGlobal(); j++ )
          ofile << output[j] << " " ;
         
        ofile << std::endl;
      }

    ofile.close();

    MPI_Finalize();
  }



  return 0;
}
