#ifndef FWDPY11_ARG_EXAMPLE_HANDLE_RECOMBINATION_HPP__
#define FWDPY11_ARG_EXAMPLE_HANDLE_RECOMBINATION_HPP__

#include <tuple>
#include <vector>
#include <fwdpy11/types.hpp>
#include "ancestry_tracker.hpp"

std::pair<std::vector<std::pair<double, double>>,
          std::vector<std::pair<double, double>>>
split_breakpoints(const std::vector<double>& breakpoints,
                  const double start = 0., const double stop = 1.);

KTfwd::uint_t
ancestry_recombination_details(
    fwdpy11::singlepop_t& pop, ancestry_tracker& ancestry,
    std::queue<std::size_t>& gamete_recycling_bin,
    const KTfwd::uint_t parental_gamete1, const KTfwd::uint_t parental_gamete2,
	const std::vector<double> & breakpoints,
    const std::tuple<ancestry_tracker::integer_type,
                     ancestry_tracker::integer_type>& pid,
    const std::tuple<ancestry_tracker::integer_type,
                     ancestry_tracker::integer_type>& offspring_indexes);

#endif
